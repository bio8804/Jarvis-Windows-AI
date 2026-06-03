import os
import subprocess

APPS = {
    'telegram': 'Telegram.exe',
    'chrome': 'chrome.exe',
    'word': 'winword.exe',
    'excel': 'excel.exe',
    'notepad': 'notepad.exe'
}


def launch_app(name):
    name = name.lower()

    if name not in APPS:
        return False

    try:
        subprocess.Popen(APPS[name])
        return True
    except Exception:
        return False
