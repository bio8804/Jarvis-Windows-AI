import speech_recognition as sr
import pyttsx3
import datetime
import os
from config import WAKE_WORD, VOICE_RATE, VOICE_VOLUME

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty('rate', VOICE_RATE)
engine.setProperty('volume', VOICE_VOLUME)


def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю...")
        audio = r.listen(source, timeout=5)
    try:
        text = r.recognize_google(audio, language='ru-RU')
        print(f"Вы: {text}")
        return text.lower()
    except:
        return None

def main():
    speak("Привет, я Jarvis. Чем могу помочь?")
    while True:
        command = listen()
        if command and WAKE_WORD in command:
            speak("Да, сэр?")
            # Здесь будет обработка команд
            if "время" in command:
                now = datetime.datetime.now().strftime("%H:%M")
                speak(f"Сейчас {now}")
            elif "пока" in command or "выход" in command:
                speak("До свидания!")
                break

if __name__ == "__main__":
    main()
