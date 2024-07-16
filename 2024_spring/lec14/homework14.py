import datetime
from gtts import gTTS
import random
import calendar
import speech_recognition as sr

def what_time_is_it(lang, filename):
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M")
    tts = gTTS(text=time_str, lang=lang)
    tts.save(filename)

def tell_me_a_joke(lang, audiofile):
    if lang == 'en':
        jokes_file = 'jokes_en.txt'
    elif lang == 'ja':
        jokes_file = 'jokes_ja.txt'
    elif lang == 'zh':
        jokes_file = 'jokes_zh.txt'
    else:
        raise ValueError("Unsupported language")

    with open(jokes_file, 'r', encoding='utf-8') as file:
        jokes = file.readlines()
    
    joke = random.choice(jokes).strip()
    tts = gTTS(text=joke, lang=lang)
    tts.save(audiofile)

def what_day_is_it(lang, audiofile):
    now = datetime.datetime.now()
    day_str = now.strftime("%A, %d %B %Y")
    tts = gTTS(text=day_str, lang=lang)
    tts.save(audiofile)
    url = f"https://www.timeanddate.com/calendar/?year={now.year}&month={now.month}"
    return url

def personal_assistant(lang, filename):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio, language=lang)
        print("You said: " + command)
        
        if "time" in command.lower():
            what_time_is_it(lang, filename)
        elif "day" in command.lower():
            what_day_is_it(lang, filename)
        elif "joke" in command.lower():
            tell_me_a_joke(lang, filename)
        else:
            print("Sorry, I didn't understand that.")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
