# Jarvis AI Voice Assistant

A Windows desktop voice assistant that listens for spoken commands and can tell the time/date, open websites, search Google, and launch Notepad or Calculator.

## Requirements
- Windows 10 or Windows 11
- Python 3.13 (tested in the project setup)
- Microphone and speakers
- Internet connection for Google speech recognition and web searches

## Setup (PowerShell)
Open PowerShell in this project folder and run:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

If PowerShell blocks activation, you can avoid activation and run:

```powershell
py -3.13 -m pip install -r requirements.txt
py -3.13 main.py
```

## Supported voice commands
- "Hello"
- "What is the time?"
- "What is the date?"
- "Open Google"
- "Open YouTube"
- "Search for Python tutorials"
- "Open website example.com"
- "Open Notepad"
- "Open Calculator"
- "Help"
- "Stop assistant" or "Exit"

## Notes
- Speech recognition uses Google's online recognition service, so an internet connection is required.
- On Windows, spoken responses use the built-in PowerShell System.Speech service.
- The microphone is used while the program is running; this is not an always-on background assistant.
- The assistant currently supports the commands listed above; it does not provide general ChatGPT-style answers.
