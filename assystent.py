# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ░╔████╗░░ ░╔██████ ░╔██████ ██╗░░░░╔██ ░╔██████ ███████████ ████████░ ██══╗░░░██ ███████████    #
# ██╔═══██╗ ██╔════╝ ██╔════╝ ░░██╗╔██╔╝ ██╔════╝ ╚═══███╔══╝ ██════╗░░ ████╚═╗░██ ╚═══███╔══╝    #
# ██║░░░██║ ░╚████╗░ ░╚████╗░ ░░░░██╔═╝░ ░╚████╗░ ░░░░███║░░░ ██████║░░ ██╔╗██║░██ ░░░░███║░░░    #
# ████████║ ░░╚══╗██ ░░╚══╗██ ░░░░██║░░░ ░░╚══╗██ ░░░░███║░░░ ██╔═══╝░░ ██║║██║░██ ░░░░███║░░░    #
# ██╔═══██║ ░░░░░║██ ░░░░░║██ ░░░░██║░░░ ░░░░░║██ ░░░░███║░░░ ██╚═════╗ ██║╚═╗████ ░░░░███║░░░    #
# ██║░░░██║ ██████╔╝ ██████╔╝ ░░░░██║░░░ ██████╔╝ ░░░░███║░░░ ████████║ ██║░░╚═╗██ ░░░░███║░░░    #
# ╚═╝░░░╚═╝ ╚═════╝░ ╚═════╝░ ░░░░╚═╝░░░ ╚═════╝░ ░░░░╚══╝░░░ ╚═══════╝ ╚═╝░░░░╚═╝ ░░░░╚══╝░░░2.0 #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

av = 0.5
ar = 190

def assystent():
    engine = pyttsx3.init()
    engine.setProperty('volume', av)
    engine.setProperty('rate', ar)
    engine.setProperty('gender', 'male')

    def opowiedz_dowcip():
        dowcipy = [
            "Dlaczego komputerowi nigdy nie jest zimno? Bo zawsze ma Windows!",
            "Dlaczego książka nie umie być spokojna? Bo zawsze ma swoją stronę!",
            "Co mówi książka do drugiej książki? Spotkamy się w bibliotece!",
            "Dlaczego Python nie lubi kawy? Bo zawsze ma problem z Java!",
            "Dlaczego niektóre programy nie idą na wakacje? Bo boją się błędów!",
        ]

        dowcip = random.choice(dowcipy)
        print("Dowcip dnia:")
        print(dowcip)
        engine.say(dowcip)
        engine.runAndWait()

    while True:
        przywitania_lista = ['cześć', 'hej', 'siema', 'hejo', 'doberek', 'dzień dobry', 'dobry']
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

                if 'przeglądarkę' in text:
                    engine.say('Otwieram przeglądarkę')
                     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                    # musisz tu podać ścierzkę przeglądarki z jakiej będziesz korzystać                      #
                    # ja kożystam z opery wiec dałem operaGx_path w nazwie ścierzki ty możesz dać inną nazwe #
                    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                    operaGx_path = r'C:/Users/User/AppData/Local/Programs/Opera GX/launcher.exe'
                    try:
                        subprocess.Popen([operaGx_path, "http://www.google.com"])
                    except Exception as e:
                        print("Błąd uruchamiania przeglądarki:", e)

                elif 'discord' in text:
                    engine.say('Otwieram Discord')
                    webbrowser.open("https://discord.com")

                elif 'spotify' in text:
                    engine.say('Otwieram Spotify')
                    webbrowser.open("https://spotify.com")

                elif 'youtube' in text:
                    engine.say('Otwieram YouTube')
                    webbrowser.open("https://www.youtube.com")

                elif 'netflix' in text:
                    engine.say('Otwieram Netflix')
                    webbrowser.open("https://www.netflix.com")

                elif 'czat gpt' in text:
                    engine.say('Otwieram chatGPT')
                    webbrowser.open("https://www.chatGPT.com")

                elif 'twitcha' in text:
                    engine.say('Otwieram twitcha')
                    webbrowser.open("https://www.twitch.com")
                elif 'tiktoka' in text:
                    engine.say('Otwieram tiktoka')
                    webbrowser.open("https://www.tiktok.com")
                elif 'replit' in text:
                    engine.say('Otwieram replita')
                    webbrowser.open("https://www.replit.com")
                elif 'github' in text:
                    engine.say('Otwieram github')
                    webbrowser.open("https://www.github.com")
                else:
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
            lp = random.randint(1, 7)

            if lp == 1:
                engine.say(przywitania_lista[0])
                engine.runAndWait()
            if lp == 2:
                engine.say(przywitania_lista[1])
                engine.runAndWait()
            if lp == 3:
                engine.say(przywitania_lista[2])
                engine.runAndWait()
            if lp == 4:
                engine.say(przywitania_lista[3])
                engine.runAndWait()
            if lp == 5:
                engine.say(przywitania_lista[4])
                engine.runAndWait()
            if lp == 6:
                engine.say(przywitania_lista[5])
                engine.runAndWait()
            if lp == 7:
                engine.say(przywitania_lista[6])
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


print('░╔████╗░░ ░╔██████ ░╔██████ ██╗░░░░╔██ ░╔██████ ███████████ ████████░ ██══╗░░░██ ███████████\n'
      '██╔═══██╗ ██╔════╝ ██╔════╝ ░░██╗╔██╔╝ ██╔════╝ ╚═══███╔══╝ ██════╗░░ ████╚═╗░██ ╚═══███╔══╝\n'
      '██║░░░██║ ░╚████╗░ ░╚████╗░ ░░░░██╔═╝░ ░╚████╗░ ░░░░███║░░░ ██████║░░ ██╔╗██║░██ ░░░░███║░░░\n'
      '████████║ ░░╚══╗██ ░░╚══╗██ ░░░░██║░░░ ░░╚══╗██ ░░░░███║░░░ ██╔═══╝░░ ██║║██║░██ ░░░░███║░░░\n'
      '██╔═══██║ ░░░░░║██ ░░░░░║██ ░░░░██║░░░ ░░░░░║██ ░░░░███║░░░ ██╚═════╗ ██║╚═╗████ ░░░░███║░░░\n'
      '██║░░░██║ ██████╔╝ ██████╔╝ ░░░░██║░░░ ██████╔╝ ░░░░███║░░░ ████████║ ██║░░╚═╗██ ░░░░███║░░░\n'
      '╚═╝░░░╚═╝ ╚═════╝░ ╚═════╝░ ░░░░╚═╝░░░ ╚═════╝░ ░░░░╚══╝░░░ ╚═══════╝ ╚═╝░░░░╚═╝ ░░░░╚══╝░░░2.0')

aname = input('jakie chcesz nadać imie swojemu asystentowi(podaj małymi literami): ')

ioa = int(input('\ninstrukcja(1) przejdź do assystenta(2) ustawienia(3) wyjdź(4): '))

if ioa == 1:
    print(f'MOŻLIWOŚCI:\n'
          f'Otwieranie stron w przeglądarce:\n'
          f'  =>Otwieranie przegladarki (powiedz {aname} otwórz/uruchom przeglądarkę)\n'
          f'  =>Otwieranie TikToka (powiedz {aname} otwórz/uruchom tiktoka)\n'
          f'  =>Otwieranie Netflixa (powiedz {aname} otwórz/uruchom netflix)\n'
          f'  =>Otwieranie youtuba (powiedz {aname} otwórz/uruchom youtube)\n'
          f'  =>Otwieranie githuba (powiedz {aname} otwórz/uruchom github)\n'
          f'  =>Otwieranie replit (powiedz {aname} otwórz/uruchom replit)\n'
          f'  =>Otwieranie spotify (powiedz {aname} otwórz/uruchom spotify)\n'
          f'  =>Otwieranie chatu GPT (powiedz {aname} otwórz/uruchom czat gpt)\n'
          f'  =>Otwieranie discorda (powiedz {aname} otwórz/uruchom discord)\n'
          f'  =>Otwieranie twitcha (powiedz {aname} otwórz/uruchom twitcha)\n'
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
