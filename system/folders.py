import os
import subprocess


def open_downloads():
    subprocess.Popen(['explorer', os.path.join(os.path.expanduser('~'), 'Downloads')])


def open_documents():
    subprocess.Popen(['explorer', os.path.join(os.path.expanduser('~'), 'Documents')])


def open_desktop():
    subprocess.Popen(['explorer', os.path.join(os.path.expanduser('~'), 'Desktop')])
