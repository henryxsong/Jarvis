#class Engine(object):
import pyttsx3
import speech_recognition as sr
from random import choice
#from utils import opening_text
from decouple import config
from datetime import datetime
from database import performing_task

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init()

engine.setProperty('rate', 200)
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

def take_user_input() -> str:
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    #TODO: add variation of responses
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-us')
        if not 'exit' in query or 'stop' in query or 'quit' in query:
            speak(query)
            speak(choice(performing_task))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query

def main():
    speak("Initiating...")
    greet_user()
    while True:
        take_user_input()

if __name__ == '__main__':
    main()