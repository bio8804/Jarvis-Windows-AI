import speech_recognition as sr
import pyttsx3
from config import WAKE_WORD, VOICE_RATE, VOICE_VOLUME, AI_PROVIDER
from ai.chat_memory import ChatMemory

engine = pyttsx3.init()
engine.setProperty('rate', VOICE_RATE)
engine.setProperty('volume', VOICE_VOLUME)

memory = ChatMemory(provider=AI_PROVIDER)


def speak(text):
    print(f'Jarvis: {text}')
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Слушаю...')
        audio = recognizer.listen(source, timeout=5)

    try:
        text = recognizer.recognize_google(audio, language='ru-RU')
        print(f'Вы: {text}')
        return text
    except Exception:
        return None


def main():
    speak('Jarvis запущен.')

    while True:
        command = listen()

        if not command:
            continue

        cmd = command.lower()

        if 'выход' in cmd or 'пока' in cmd:
            speak('До свидания!')
            break

        if WAKE_WORD in cmd:
            prompt = cmd.replace(WAKE_WORD, '').strip()

            if not prompt:
                speak('Слушаю вас.')
                continue

            try:
                answer = memory.ask(prompt)
                speak(answer)
            except Exception as e:
                speak('Ошибка подключения к языковой модели.')
                print(e)


if __name__ == '__main__':
    main()
