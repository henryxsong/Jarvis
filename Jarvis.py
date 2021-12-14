#class Engine(object):
import pyttsx3
from decouple import config

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