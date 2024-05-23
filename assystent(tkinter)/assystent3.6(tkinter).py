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
# pip instal , SpeechRecognition, pyttsx3, requests, win10toast_persist, wikipedia, pyAudio #
#############################################################################################
import webbrowser, pyttsx3, subprocess, requests, pyautogui, time, wikipedia, random, sys, datetime, ctypes, pyttsx3.drivers.sapi5
import tkinter as tk
import speech_recognition as sr
from win10toast import ToastNotifier
from tkinter import messagebox
from mtranslate import translate

def assistant():
    global aname, av, ar
    engine = pyttsx3.init()
    engine.setProperty('volume', av)
    engine.setProperty('rate', ar)
    engine.setProperty('gender', 'male')

    # lista powitań
    greetings_list = ['cześć', 'hej', 'siema', 'hejo', 'doberek', 'dzień dobry', 'dobry']

    # podstawowe ustawienia assystenta
    av = 0.5
    ar = 190

    # komendy aby assystent powiedział żart
    tell_joke_command = [
        'opowiedz dowcip',
        'opowiedz żart',
        'powiedz dowcip',
        'powiedz żart'
    ]

    # data i czas
    def date_and_time():
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Aktualna godzina: {current_time}")

    # zegar
    def clock():
        def update_clock():
            ora_curenta = time.strftime('%H:%M:%S')
            ceas.config(text=ora_curenta)
            ceas.after(1000, update_clock)

        app = tk.Tk()
        app.title('zegar python')

        ceas = tk.Label(app, text='', font=('Helvetica', 48))
        ceas.pack()

        update_clock()
        app.mainloop()

    # tłumaczenie textu
    def translate_text(text, target_language='en'):
        translated_text = translate(' '.join(text[1:]), target_language)
        return translated_text

    # żarty
    def tell_joke():
        jokes = [
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

        joke = random.choice(jokes)
        print("Dowcip dnia:")
        print(joke)
        engine.say(joke)
        engine.runAndWait()

    # powitania
    def greetings():
        random_greetings = random.choice(greetings_list)
        print(random_greetings)
        engine.say(random_greetings)
        engine.runAndWait()

    #główna pętla
    while True:

        # rozpoznawanie mowy i ustawienia rozpoznawania
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
        notes = []

        # dodawanie notatek
        def add_note(note):
            try:
                notes.append(note)
                print('Dodano notatkę:', note)
            except Exception as e:
                print('Nie udało się dodać notatki:', e)

        # czytanie notatek (kiedyś siądę i naprawię)
        def read_notes():
            if not notes:
                print('Brak notatek.')
            else:
                print('Twoje notatki:')
                for i, note in enumerate(notes, start=1):
                    print(f'{i}. {note}')
                    engine.say(note)
                    engine.runAndWait()

        # wzywanie assystenta
        if (aname.get().lower() in text and word_list[0] == aname.get().lower()):

            # otwieranie stron
            if ("otwórz" in text and word_list[1] == 'otwórz') or ("uruchom" in text and word_list[1] == 'uruchom'):

                # rozpoznawanie stron i ich otwieranie
                if 'przeglądarkę' in text:
                    engine.say('Otwieram przeglądarkę')
                    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                    # Musisz tu podać ścieżkę przeglądarki z jakiej będziesz korzystać                      #
                    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                    operaGx_path = r'C:\Users\Uzytkownik1\AppData\Local\Programs\Opera GX.exe'#<=======o tu przed .exe musisz dać tą śieżkę
                    try:
                        subprocess.Popen([operaGx_path, "http://www.google.com"])
                    except Exception as e:
                        print("Błąd uruchamiania przeglądarki:", e)

                # otwieranie yt z możliwością podawania tytułów
                elif 'youtube' in text:
                    engine.say('Otwieram YouTube')
                    webbrowser.open("https://www.youtube.com")
                    if 'tytuł' in text:
                        tytul = ' '.join(word_list[4:])
                        try:
                            time.sleep(8)
                            pyautogui.click(700, 120)
                            pyautogui.write(tytul, interval=0.1)
                            pyautogui.press('ENTER')
                        except:
                            print('coś nie pykło')

                else:
                    app_name = ' '.join(word_list[2:])
                    engine.say(f'Otwieram {app_name}')
                    webbrowser.open(f'https://www.{app_name}.com')

            # komenda na koniec programu
            elif ('koniec' in text and word_list[1] == 'koniec'):
                sys.exit(0)

            # komenda na pogodę (muszę znaleźć API)
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

            # artykuły
            elif 'artykuł' in text and len(word_list) >= 4 and word_list[0:2] == ['pokaż', 'mi']:
                wikipedia.set_lang('pl')
                phrase = ' '.join(word_list[3:])
                try:
                    page = wikipedia.page(phrase)
                    webbrowser.open_new_tab(page.url)
                except wikipedia.exceptions.PageError:
                    print("Nie znaleziono strony dla podanej frazy.")
                else:
                    print("Warunki nie zostały spełnione. Nie można kontynuować.")

            # funkja do pisania
            elif 'pisz' in text:
                sentences = ' '.join(word_list[2:])
                try:
                    time.sleep(5)
                    pyautogui.typewrite(sentences, interval=0.05)
                except Exception as e:
                    print('Nie można wykonać czynności. Błąd:', e)

            # funkcja do liczenia
            elif 'licz' in text:
                try:
                    expression = ' '.join(word_list[2:])
                    result = eval(expression)
                    engine.say(f'wynik to {result}')
                    engine.runAndWait()
                    print(f'wynik to {result}')
                except Exception as e:
                    print('Błąd kalkulatora. Spróbuj ponownie. Błąd:', e)

            # opowiadanie żartu
            elif any(tell_joke_command):
                tell_joke()

            # dodaj notatkę
            elif 'dodaj notatkę' in text:
                try:
                    note = ' '.join(word_list[3:])
                    add_note(note)
                except:
                    print('Nie udało się zapisać notatki.')

            # czytaj notatkę
            elif 'odczytaj notatkę' in text:
                read_notes()

            # data i czas
            elif 'data i czas' in text:
                date_and_time()

            # zegar
            elif 'zegar' in text:
                clock()

            # tłumaczenie
            elif 'tłumacz' in text:
                translated_text = translate_text(word_list, target_language='en')
                print(f"Tłumaczenie: {translated_text}")
                engine.say(translated_text)
                engine.runAndWait()

            # powitania
            elif any(greeting.lower() in word_list[1] for greeting in greetings_list):
                greetings()

# funkcja kończenia pracy
def end():
    sys.exit(0)

# funkcja ustawień
def settings():
    global ar, av
    settings_window = tk.Tk()
    settings_window.title('ustawienia')

    glosnosc = tk.Label(settings_window, text='podaj glosność assystenta')
    glosnosc.pack()

    av = tk.Entry(settings_window)
    av.pack()

    predkosc = tk.Label(settings_window, text='podaj prędkość assystenta')
    predkosc.pack()

    ar = tk.Entry(settings_window)
    ar.pack()

    # zapisywanie ustawień
    def save_settings():
        global ar, av
        av = float(av.get())
        ar = int(ar.get())
        settings_window.destroy()

    zapisz_button = tk.Button(settings_window, text="Zapisz", command=save_settings)
    zapisz_button.pack()

    settings_window.mainloop()

# fuckcjonowanie assystenta
def assistent_function():
    messagebox.showinfo('assystent', 'powiedz coś')
    assistant()

# instrukcja
def info():
    messagebox.showinfo("Instrukcja", '''
        MOŻLIWOŚCI:\n'
         =>Otwieranie przeglądarki(powiedz imię asystenta, otwórz/uruchom i powiedz przeglądarkę)
         =>Otwieranie YT z możliwością podania tytułu(powiedz imię assystenta, uruchom/otwórz Youtube, jeśli chcesz dodaj "tytuł <tytuł który chcesz>")
         =>Otwieranie dowolnej strony (poweidz imię asystenta i stronę jaką chcesz otworzyć)
         =>Wyjśćie z programu (powiedz imię asystenta i dodaj "koniec")
       INNE możliwości:
         =>Witanie się (powiedz imię asystenta i siema/hej/cześć a assystent ci odpowie losowo wybranym przywitaniem)
         =>Pogoda (powiedz imię asystenta i "jaka jest pogoda" a wtedy w powiadomieniu przyjdzie ci temperatura, odczuwalna temp,
             ciśnienie i wilgotność)
         =>Artykuły z wikipedi (powiedz imię asystenta i "pokaż mi artykuł <nazwa artykułu jaki chcesz przeczytać>")
         =>Pisanie z mowy (powiedz imię asystenta i "pisz" i to co chcesz żeby assystent napisał a później przejdź do komunikatora i 
           naciśnij na miejsce do wpisywania textu)
        =>Tłumaczenie z mowy (powiedz imię asystenta i "tłumacz" i to co chcesz powiedzieć a {aname} ci to przetłumaczy i przeczyta)
        =>Zegar (po powiedzeniu imię asystenta i 'zegar' pojawi się okienko z zegarem)
        =>Data i czas (po imię asystenta i 'powiedzeniu Data i czas' w terminalu pojawi się dokładny rok, dzień, miesiąc, gadzina, minuta,
            sekunda)
        =>Notatki (po powiedzeniu imienia asystenta i 'dodaj notatkę' powiedz co chcesz zanotować)
        =>Odczytaj notatke (po powiedzeniu imienia asystenta i 'odczytaj notatkę' {aname} napisze i odczyta ostatnią notatkę)
        =>Licz (po powiedzeniu imienia asystenta i 'licz' powiedz działanie jakie chcesz żeby {aname} odczytał)
       INSTRUKCJA:
         =>musisz mówić tak jak jest podane w MOŻLIWOŚCIACH
         =>masz 60 sekund na powiedzenie polecenia dla assystenta
         =>jeżeli assystent nie zrozumie tego co powiedziałeś napisze ci że nie zrozumiał i sie wyłączy 
         =>program moze się ścinać ponieważ ma dużo rzeczy do przetworzenia
         =>to co mówisz i to co ci odpowie assystent wyświetla się w terminalu
    ''')
    assistent_function()

# główne okno
aapp = tk.Tk()
aapp.title('assystent')

# logo assystenta
logo = tk.Label(text='''
 ░╔████╗░░ ░╔██████ ░╔██████ ██╗░░░░╔██ ░╔██████ ███████████ ████████░ ██══╗░░░██ ███████████ 
 ██╔═══██╗ ██╔════╝ ██╔════╝ ░░██╗╔██╔╝ ██╔════╝ ╚═══███╔══╝ ██════╗░░ ████╚═╗░██ ╚═══███╔══╝ 
 ██║░░░██║ ░╚████╗░ ░╚████╗░ ░░░░██╔═╝░ ░╚████╗░ ░░░░███║░░░ ██████║░░ ██╔╗██║░██ ░░░░███║░░░ 
 ████████║ ░░╚══╗██ ░░╚══╗██ ░░░░██║░░░ ░░╚══╗██ ░░░░███║░░░ ██╔═══╝░░ ██║║██║░██ ░░░░███║░░░ 
 ██╔═══██║ ░░░░░║██ ░░░░░║██ ░░░░██║░░░ ░░░░░║██ ░░░░███║░░░ ██╚═════╗ ██║╚═╗████ ░░░░███║░░░ 
 ██║░░░██║ ██████╔╝ ██████╔╝ ░░░░██║░░░ ██████╔╝ ░░░░███║░░░ ████████║ ██║░░╚═╗██ ░░░░███║░░░ 
 ╚═╝░░░╚═╝ ╚═════╝░ ╚═════╝░ ░░░░╚═╝░░░ ╚═════╝░ ░░░░╚══╝░░░ ╚═══════╝ ╚═╝░░░░╚═╝ ░░░░╚══╝░░░
''')
logo.pack()

# entry do dawania imienia assystentowi
aname = tk.Entry()
aname.pack()

# uruchamianie funkcjonowania assystenta
astntb = tk.Button(text='assystent', command=assistent_function)
astntb.pack()

# otwieranie instrukcji
infob = tk.Button(text='informacje/instrukcja', command=info)
infob.pack()

# otwieranie ustawień
settingsb = tk.Button(text='ustawienia', command=settings)
settingsb.pack()

# przycisk kończenia
endb = tk.Button(text='koniec', command=end)
endb.pack()

# pętla okna
aapp.mainloop()
