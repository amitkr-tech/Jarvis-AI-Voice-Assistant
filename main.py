
import datetime
import platform
import subprocess
import webbrowser
import speech_recognition as sr

def speak(text):
    print("Assistant:", text)

    if platform.system() == "Windows":
        safe_text = text.replace("'", "''")
        command = (
            "Add-Type -AssemblyName System.Speech; "
            "$s = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
            f"$s.Speak('{safe_text}')"
        )
        subprocess.run(
            ["powershell.exe", "-NoProfile", "-Command", command],
            check=False
        )

def handle(command):
    if not command:
        return True

    if any(x in command for x in ["exit", "quit", "stop assistant", "goodbye"]):
        speak("Goodbye!")
        return False

    if "hello" in command or command == "hi":
        speak("Hello! How can I help?")
    elif "time" in command:
        speak("The time is " + datetime.datetime.now().strftime("%I:%M %p"))
    elif "date" in command:
        speak("Today is " + datetime.date.today().strftime("%d %B %Y"))
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif command.startswith("search for "):
        q = command.replace("search for ", "", 1).strip()
        webbrowser.open("https://www.google.com/search?q=" + q.replace(" ", "+"))
        speak("Searching Google for " + q)
    elif command.startswith("open website "):
        site = command.replace("open website ", "", 1).strip()
        if site:
            if not site.startswith(("http://", "https://")):
                site = "https://" + site
            webbrowser.open(site)
            speak("Opening website")
    elif "open notepad" in command and platform.system() == "Windows":
        subprocess.Popen(["notepad.exe"])
        speak("Opening Notepad")
    elif "open calculator" in command and platform.system() == "Windows":
        subprocess.Popen(["calc.exe"])
        speak("Opening Calculator")
    elif "help" in command:
        speak("Try: what is the time, what is the date, open Google, open YouTube, search for Python tutorials, open Notepad, or stop assistant.")
    else:
        speak("I do not have that action yet. Say help for supported commands.")

    return True

def main():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    speak("Voice Controlled Personal Assistant is ready. Say help for commands.")

    while True:
        with mic as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
            except sr.WaitTimeoutError:
                continue

        try:
            command = recognizer.recognize_google(audio).lower().strip()
            print("You:", command)
        except sr.UnknownValueError:
            speak("Sorry, please repeat.")
            continue
        except sr.RequestError:
            speak("Speech service unavailable. Check internet.")
            continue

        if not handle(command):
            break

if __name__ == "__main__":
    try:
        main()
    except OSError as e:
        print("Audio/microphone error:", e)
        print("Connect and enable a microphone, then try again.")
