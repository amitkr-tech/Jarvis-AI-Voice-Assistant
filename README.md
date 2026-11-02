# Voice-Controlled Personal Assistant

## Requirements
Windows 10/11 recommended, Python 3.10/3.11, microphone, speakers and internet.

## Run (Windows Command Prompt)
```bash
py -3.11 -m venv .venv
.venv\\Scripts\\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

If PyAudio installation fails, check that Python is 64-bit and version 3.10/3.11.
You can try `python -m pip install pipwin` then `pipwin install pyaudio`.

## Commands
- hello
- what is the time / what is the date
- open Google / open YouTube
- search for Python tutorials
- open website example.com
- open Notepad / open Calculator (Windows)
- help
- stop assistant / exit

Speech recognition uses Google's online service and needs internet. The assistant
listens only while the program is running; it is not an always-on background service.
