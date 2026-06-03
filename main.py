import speech_recognition as sr
import pyttsx3
from config import WAKE_WORD, VOICE_RATE, VOICE_VOLUME, AI_PROVIDER
from ai.chat_memory import ChatMemory
from skills.app_launcher import launch_app
from system.power import shutdown_pc, restart_pc, lock_pc
from system.folders import open_downloads, open_documents, open_desktop

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
        audio = recognizer.listen(source, timeout=5)

    try:
        return recognizer.recognize_google(audio, language='ru-RU')
    except Exception:
        return None


def process_local_command(prompt):
    apps = ['telegram', 'chrome', 'word', 'excel', 'notepad']

    if 'открой загрузки' in prompt:
        open_downloads()
        return 'Открываю загрузки'

    if 'открой документы' in prompt:
        open_documents()
        return 'Открываю документы'

    if 'открой рабочий стол' in prompt:
        open_desktop()
        return 'Открываю рабочий стол'

    if 'выключи компьютер' in prompt:
        shutdown_pc()
        return 'Выключаю компьютер'

    if 'перезагрузи компьютер' in prompt:
        restart_pc()
        return 'Перезагружаю компьютер'

    if 'заблокируй компьютер' in prompt:
        lock_pc()
        return 'Блокирую компьютер'

    if 'открой' in prompt:
        for app in apps:
            if app in prompt:
                if launch_app(app):
                    return f'Открываю {app}'

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

            local_result = process_local_command(prompt)

            if local_result:
                speak(local_result)
                continue

            try:
                speak(memory.ask(prompt))
            except Exception as e:
                speak('Ошибка подключения к языковой модели.')
                print(e)


if __name__ == '__main__':
    main()
