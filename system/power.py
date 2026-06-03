import os
import ctypes


def shutdown_pc():
    os.system('shutdown /s /t 0')


def restart_pc():
    os.system('shutdown /r /t 0')


def lock_pc():
    ctypes.windll.user32.LockWorkStation()
