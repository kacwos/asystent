# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ░╔████╗░░ ░╔██████ ░╔██████ ██╗░░░░╔██ ░╔██████ ███████████ ████████░ ██══╗░░░██ ███████████ #
# ██╔═══██╗ ██╔════╝ ██╔════╝ ░░██╗╔██╔╝ ██╔════╝ ╚═══███╔══╝ ██════╗░░ ████╚═╗░██ ╚═══███╔══╝ #
# ██║░░░██║ ░╚████╗░ ░╚████╗░ ░░░░██╔═╝░ ░╚████╗░ ░░░░███║░░░ ██████║░░ ██╔╗██║░██ ░░░░███║░░░ #
# ████████║ ░░╚══╗██ ░░╚══╗██ ░░░░██║░░░ ░░╚══╗██ ░░░░███║░░░ ██╔═══╝░░ ██║║██║░██ ░░░░███║░░░ #
# ██╔═══██║ ░░░░░║██ ░░░░░║██ ░░░░██║░░░ ░░░░░║██ ░░░░███║░░░ ██╚═════╗ ██║╚═╗████ ░░░░███║░░░ #
# ██║░░░██║ ██████╔╝ ██████╔╝ ░░░░██║░░░ ██████╔╝ ░░░░███║░░░ ████████║ ██║░░╚═╗██ ░░░░███║░░░ #
# ╚═╝░░░╚═╝ ╚═════╝░ ╚═════╝░ ░░░░╚═╝░░░ ╚═════╝░ ░░░░╚══╝░░░ ╚═══════╝ ╚═╝░░░░╚═╝ ░░░░╚══╝░░░ #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#############################################################################################
# pip instal , SpeechRecognition, pyttsx3, requests, win10toast_persist, wikipedia #
############################################################################################
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
import datetime
import tkinter
from mtranslate import translate

av = 0.5
ar = 190

opowiedz_dowcip_komenda = [
    'opowiedz dowcip',
    'opowiedz żart',
    'powiedz dowcip',
    'powiedz żart'
]

def data_i_czas():
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Aktualna godzina: {current_time}")


def zegar():
    def update_clock():
        ora_curenta = time.strftime('%H:%M:%S')
        ceas.config(text=ora_curenta)
        ceas.after(1000, update_clock)

    app = tkinter.Tk()
    app.title('zegar python')

    ceas = tkinter.Label(app, text='', font=('Helvetica', 48))
    ceas.pack()

    update_clock()
    app.mainloop()

def translate_text(text, target_language='en'):
    translated_text = translate(' '.join(text[1:]), target_language)
    return translated_text
def assystent():
    engine = pyttsx3.init()
    engine.setProperty('volume', av)
    engine.setProperty('rate', ar)
    engine.setProperty('gender', 'male')

    def opowiedz_dowcip():
        dowcipy = [
            "Dlaczego komputerowi nigdy nie jest zimno? Bo zawsze ma Windows!",
            "Dlaczego książka nie mogła wejść do baru? Bo miała już za dużo rozdziałów!",
            "Dlaczego psy nie potrafią korzystać z komputera? Bo mają trudność z zatrzaskiwaniem myszy!",
            "Co mówi zegar do drugiego zegara? 'Hej, masz czas?'",
            "Dlaczego krowa nie potrafi grać w gry wideo? Bo zawsze rzuca się na joystick!",
            "Jak nazywa się wiewiórka ninja? Skradająca się!",
            "Dlaczego księżyc nigdy nie śpi? Bo zawsze jest w fazie!",
            "Jak nazywa się nielegalny przekręt marchewkowy? Burak!",
            "Dlaczego nie można ufać schodom? Bo są zawsze pełne podejrzeń!",
            "Jak nazywa się owca, która zna sztuki walki? Baa-rbarian!"
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
        notatki = []

        def dodaj_notatke(notka):
            try:
                notatki.append(notka)
                print('Dodano notatkę:', notka)
            except Exception as e:
                print('Nie udało się dodać notatki:', e)

        def odczytaj_notatki():
            if not notatki:
                print('Brak notatek.')
            else:
                print('Twoje notatki:')
                for i, notka in enumerate(notatki, start=1):
                    print(f'{i}. {notka}')
                    engine.say(notka)
                    engine.runAndWait()

        if (aname in text and word_list[0] == aname):
            if ("otwórz" in text and word_list[1] == 'otwórz') or ("uruchom" in text and word_list[1] == 'uruchom'):

                if 'przeglądarkę' in text:
                    engine.say('Otwieram przeglądarkę')
                     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                    # musisz tu podać ścierzkę przeglądarki z jakiej będziesz korzystać                      #
                    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                    operaGx_path = r'.exe'
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
                    if 'tytuł' in text:
                        tytul = ' '.join(word_list[4:])
                        try:
                            time.sleep(6)
                            pyautogui.click(700, 100)
                            pyautogui.write(tytul, interval=0.1)
                            pyautogui.press('ENTER')
                        except:
                            print('coś nie pykło')


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
                    app = ' '.join(word_list[2:])
                    engine.say(f'Otwieram {app}')
                    webbrowser.open(f'https://www.{app}.com')
        elif 'koniec' in text:
            sys.exit(0)

        elif text == 'jaka jest pogoda':
            with open('api_key.txt', "r") as f:
                api_key = f.read().strip()

            base_url = 'https://api.openweathermap.org/data/2.5/weather?q='
            city = 'Warszawa'
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


        elif 'pisz' in text :
            zdania = ' '.join(word_list[1:])
            try:
                time.sleep(5)
                pyautogui.typewrite(zdania, interval=0.05)
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

        elif (opowiedz_dowcip_komenda[0] in text or
              opowiedz_dowcip_komenda[1] in text or
              opowiedz_dowcip_komenda[2] in text or
              opowiedz_dowcip_komenda[3] in text) :
            opowiedz_dowcip()

        elif 'dodaj notatkę' in text:
            try:
                notka = ' '.join(word_list[2:])
                dodaj_notatke(notka)
            except:
                print('Nie udało się zapisać notatki.')

        elif 'odczytaj notatkę' in text:
            odczytaj_notatki()

        elif 'data i czas' in text:
            data_i_czas()

        elif 'zegar' in text:
            zegar()

        elif 'tłumacz' in text:
            translated_text = translate_text(word_list, target_language='en')
            print(f"Tłumaczenie: {translated_text}")
            engine.say(translated_text)
            engine.runAndWait()



print('░╔████╗░░ ░╔██████ ░╔██████ ██╗░░░░╔██ ░╔██████ ███████████ ████████░ ██══╗░░░██ ███████████\n'
      '██╔═══██╗ ██╔════╝ ██╔════╝ ░░██╗╔██╔╝ ██╔════╝ ╚═══███╔══╝ ██════╗░░ ████╚═╗░██ ╚═══███╔══╝\n'
      '██║░░░██║ ░╚████╗░ ░╚████╗░ ░░░░██╔═╝░ ░╚████╗░ ░░░░███║░░░ ██████║░░ ██╔╗██║░██ ░░░░███║░░░\n'
      '████████║ ░░╚══╗██ ░░╚══╗██ ░░░░██║░░░ ░░╚══╗██ ░░░░███║░░░ ██╔═══╝░░ ██║║██║░██ ░░░░███║░░░\n'
      '██╔═══██║ ░░░░░║██ ░░░░░║██ ░░░░██║░░░ ░░░░░║██ ░░░░███║░░░ ██╚═════╗ ██║╚═╗████ ░░░░███║░░░\n'
      '██║░░░██║ ██████╔╝ ██████╔╝ ░░░░██║░░░ ██████╔╝ ░░░░███║░░░ ████████║ ██║░░╚═╗██ ░░░░███║░░░\n'
      '╚═╝░░░╚═╝ ╚═════╝░ ╚═════╝░ ░░░░╚═╝░░░ ╚═════╝░ ░░░░╚══╝░░░ ╚═══════╝ ╚═╝░░░░╚═╝ ░░░░╚══╝░░░')

aname = input('jakie chcesz nadać imie swojemu asystentowi(podaj małymi literami): ')

ioa = int(input('\ninstrukcja(1) przejdź do assystenta(2) ustawienia(3) wyjdź(4): '))

if ioa == 1:
    print(f'''
        MOŻLIWOŚCI:\n'
         =>Otwieranie stron w przeglądarce:'
         =>Otwieranie przegladarki (powiedz {aname} otwórz/uruchom przeglądarkę)
         =>Otwieranie TikToka (powiedz {aname} otwórz/uruchom tiktoka)
         =>Otwieranie Netflixa (powiedz {aname} otwórz/uruchom netflix)
         =>Otwieranie youtuba (powiedz {aname} otwórz/uruchom youtube, możesz też dodać "tytuł" i powiedzieć a {aname} wpisze w wyszukiwarce tytuł który powiedziałeś)
         =>Otwieranie githuba (powiedz {aname} otwórz/uruchom github)
         =>Otwieranie replit (powiedz {aname} otwórz/uruchom replit)
         =>Otwieranie spotify (powiedz {aname} otwórz/uruchom spotify)
         =>Otwieranie chatu GPT (powiedz {aname} otwórz/uruchom czat gpt)
         =>Otwieranie discorda (powiedz {aname} otwórz/uruchom discord)
         =>Otwieranie twitcha (powiedz {aname} otwórz/uruchom twitcha)
         =>Otwieranie dowolnej strony (poweidz stronę jaką chcesz otworzyć)
         =>Wyjśćie z programu (powiedz "koniec")
       INNE możliwości:
         =>Witanie się (powiedz siema/hej/cześć a assystent ci odpowie losowo wybranym przywitaniem)
         =>Pogoda (powiedz "jaka jest pogoda" a wtedy w powiadomieniu przyjdzie ci temperatura, odczuwalna temp,
             ciśnienie i wilgotność)
         =>Artykuły z wikipedi (powiedz "pokaż mi artykuł <nazwa artykułu jaki chcesz przeczytać>")
         =>Pisanie z mowy (powiedz "pisz" i to co chcesz żeby assystent napisał a później przejdź do komunikatora i 
           naciśnij na miejsce do wpisywania textu)
        =>Tłumaczenie z mowy (powiedz "tłumacz" i to co chcesz powiedzieć a {aname} ci to przetłumaczy i przeczyta)
        =>Zegar (po powiedzeniu 'zegar' pojawi się okienko z zegarem)
        =>Data i czas (po 'powiedzeniu Data i czas' w terminalu pojawi się dokładny rok, dzień, miesiąc, gadzina, minuta,
            sekunda)
        =>Notatki (po powiedzeniu 'dodaj notatkę' powiedz co chcesz zanotować)
        =>Odczytaj notatke (po powiedzeniu 'odczytaj notatkę' {aname} napisze i odczyta ostatnią notatkę)
        =>Licz (po powiedzeniu 'licz' powiedz działanie jakie chcesz żeby {aname} odczytał)
       INSTRUKCJA:
         =>musisz mówić tak jak jest podane w MOŻLIWOŚCIACH
         =>masz 60 sekund na powiedzenie polecenia dla assystenta
         =>jeżeli assystent nie zrozumie tego co powiedziałeś napisze ci że nie zrozumiał i sie wyłączy 
    ''')
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

