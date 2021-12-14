#class Engine(object):
import pyttsx3
from decouple import config
from datetime import datetime

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init()

engine.setProperty('rate', 190)
engine.setProperty('volume', 1)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id) #voices index 7 represesnts a british male voice, similar to JARVIS

def speak(txt:str) -> None:
    '''
    Synthesizes speech based on given text

    :param txt: string of text to speechify
    '''
    engine.say(txt)
    engine.runAndWait()

def greet_user() -> None:
    """
    Greets user according to time of day (morning, afternoon, evening)
    """
    current_time = datetime.now()
    current_hour = current_time.hour

    if current_hour >= 0 and current_hour < 12:
        speak(f"Good morning {USERNAME}")
    elif current_hour >= 12 and current_hour < 18:
        speak(f"Good afternoon {USERNAME}")
    elif current_hour >= 18 and current_hour < 24:
        speak(f"Good evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")

greet_user()
