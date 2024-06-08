import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

def open_browser():
    webbrowser.open("https://www.google.com")

while True:
    with sr.Microphone() as source:
        print("Говорите что-нибудь (или 'выход' для завершения)")

        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="ru-RU")
            print("Вы сказали: " + text)

            if text.lower() == "бонго":
                open_browser()
        except sr.UnknownValueError:
            print("Извините, не могу распознать речь")
        except sr.RequestError as e:
            print("Ошибка при обращении к сервису распознавания речи; {0}".format(e))

        if text.lower() == 'выход':
            break