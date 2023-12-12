import speech_recognition as sr
import webbrowser
import pyttsx3
import subprocess
import requests
from win10toast_persist import ToastNotifier
import pyautogui
import time
import wikipedia
import random
import sys

from consts import av, ar, dowcipy, przywitania_lista, version, logo, strony_lista


def assystent():
    engine = pyttsx3.init()
    engine.setProperty('volume', av)
    engine.setProperty('rate', ar)
    engine.setProperty('gender', 'male')

    def opowiedz_dowcip():
        dowcip = random.choice(dowcipy)
        print("Dowcip dnia:")
        print(dowcip)
        engine.say(dowcip)
        engine.runAndWait()

    while True:
        def recognize_speech(message='Powiedz coś'):
            recognizer = sr.Recognizer()

            try:
                with sr.Microphone() as source:
                    print(message)
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source, timeout=60)

                recognized_text = recognizer.recognize_google(audio, language='pl-PL')
                print('Powiedziałeś: ' + recognized_text)
                return recognized_text.lower()

            except sr.UnknownValueError:
                print('Nie zrozumiałem, co powiedziałeś!')
            except sr.RequestError as e:
                print("BŁĄD: ", e)
                print("Sprawdź połączenie z internetem.")
            except Exception as e:
                print("Niespodziewany błąd:", e)


        text = recognize_speech()
        word_list = text.split(" ")

        if (aname in text and word_list[0] == aname):
            if ("otwórz" in text and word_list[1] == 'otwórz') or ("uruchom" in text and word_list[1] == 'uruchom'):
                czy_strona_obslugiwana = False
                for strona in strony_lista:
                    if strona[1] in text:
                        czy_strona_obslugiwana = True
                        engine.say(f'Otwieram {strona[1]}')
                        webbrowser.open(strona[2])
                        break
                if not czy_strona_obslugiwana:
                    print('nie znam takiej aplikacji')
        elif 'koniec' in text:
            sys.exit(0)

        elif text == 'jaka jest pogoda':
            with open('api_key.txt', "r") as f:
                api_key = f.read().strip()

            base_url = 'https://api.openweathermap.org/data/2.5/weather?q='
            city = 'Lublin'
            complete_url = f'{base_url}{city}&appid={api_key}'

            try:
                response = requests.get(complete_url)
                response.raise_for_status()

                x = response.json()
                y = x['main']

                temp = y['temp']
                feels_like = y['feels_like']
                pressure = y['pressure']
                humidity = y['humidity']

                toaster = ToastNotifier()
                toaster.show_toast('Pogoda na dziś',
                                   f"Temperatura: {round(temp - 273.15)}°C\n"
                                   f"Odczuwalna temperatura: {round(feels_like - 273.15)}°C\n"
                                   f"Ciśnienie: {pressure}hPa\n"
                                   f"Wilgotność: {humidity}%",
                                   icon_path=None, duration=None)
            except requests.exceptions.HTTPError as errh:
                print("Błąd HTTP:", errh)
            except requests.exceptions.ConnectionError as errc:
                print("Błąd połączenia:", errc)
            except requests.exceptions.Timeout as errt:
                print("Błąd timeout:", errt)
            except requests.exceptions.RequestException as err:
                print("Niespodziewany błąd:", err)


        elif 'artykuł' in text and len(word_list) >= 4 and word_list[0:2] == ['pokaż', 'mi']:
            wikipedia.set_lang('pl')
            fraza = ' '.join(word_list[3:])
            try:
                strona = wikipedia.page(fraza)
                webbrowser.open_new_tab(strona.url)
            except wikipedia.exceptions.PageError:
                print("Nie znaleziono strony dla podanej frazy.")
            else:
                print("Warunki nie zostały spełnione. Nie można kontynuować.")

        elif przywitania_lista[0] in text or przywitania_lista[1] in text or przywitania_lista[2] in text:
            engine.say(random.choice(przywitania_lista))
            engine.runAndWait()

        elif 'pisz' in text:
            zdania = ' '.join(word_list[1:])
            try:
                time.sleep(5)
                pyautogui.write(zdania, interval=0.05)
            except Exception as e:
                print('Nie można wykonać czynności. Błąd:', e)

        elif 'licz' in text:
            try:
                wyrazenie = ' '.join(word_list[1:])
                wynik = eval(wyrazenie)
                engine.say(f'wynik to {wynik}')
                engine.runAndWait()
                print(f'wynik to {wynik}')
            except Exception as e:
                print('Błąd kalkulatora. Spróbuj ponownie. Błąd:', e)

        elif 'opowiedz dowcip' in text:
            opowiedz_dowcip()


print(f'{logo}{version}\n')

aname = input('Jakie chcesz nadać imię swojemu asystentowi: ').lower()

ioa = int(input('\ninstrukcja(1) przejdź do assystenta(2) ustawienia(3) wyjdź(4): '))

if ioa == 1:
    def komunikat_z_lista_stron():
        return ''.join(map(
            lambda strona: f'  =>Otwieranie {strona[0]} (powiedz {aname} otwórz/uruchom {strona[1]})\n',
            strony_lista
        ))

    print(f'MOŻLIWOŚCI:\n'
          f'Otwieranie stron w przeglądarce:\n' +
          komunikat_z_lista_stron() +
          '  =>Wyjśćie z programu (powiedz "koniec")\n\n'
          'INNE możliwości:\n'
          '  =>Witanie się (powiedz siema/hej/cześć a assystent ci odpowie losowo wybranym przywitaniem)\n'
          '  =>Pogoda (powiedz "jaka jest pogoda" a wtedy w powiadomieniu przyjdzie ci temperatura, odczuwalna temp,'
          ' ciśnienie i wilgotność)\n'
          '  =>artykuły z wikipedi (powiedz "pokaż mi artykuł <nazwa artykułu jaki chcesz przeczytać>")\n'
          '  =>pisanie z mowy (powiedz "pisz" i to co chcesz żeby assystent napisał a później przejdź do komunikatora i '
          'naciśnij na miejsce do wpisywania textu)\n\n'
          'INSTRUKCJA:\n'
          '  =>musisz mówić tak jak jest podane w MOŻLIWOŚCIACH\n'
          '  =>masz 60 sekund na powiedzenie polecenia dla assystenta\n'
          '  =>jeżeli assystent nie zrozumie tego co powiedziałeś napisze ci że nie zrozumiał i sie wyłączy')
    time.sleep(30)
    assystent()
if ioa == 2:
    assystent()
if ioa == 3:
    print('ustawienia:\n (1)głośność\n (2)prędkość')
    ua = int(input('co chcesz zmienić: '))
    if ua == 1:
        print('mozesz zmienić głośność od 0 do 10')
        av = float(input('na jaką wartość chcesz zmienić głośność: '))
        print(f'zmieniłeś głośność na {av}')
        time.sleep(5)
        assystent()
    if ua == 2:
        print('możesz zmieniać predkość od 100 do 500')
        ar = float(input('na jaka wartość chcesz zmienić prędkość: '))
        print(f'zmieniłeś prędkość na {ar}')
        time.sleep(5)
        assystent()
    else:
        print('zła odpowiedź assystent sie za 3 sekundy wyłączy')
        time.sleep(3)
if ioa == 4:
    sys.exit(0)

else:
    print('zła odpowiedź assystent sie za 3 sekundy wyłączy')
    time.sleep(3)
