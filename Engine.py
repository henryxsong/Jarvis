#class Engine(object):
import pyttsx3
import speech_recognition as sr
from random import choice
from decouple import config
from datetime import datetime
from phrase_database import performing_task

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

class Engine(object):
    def __init__(self) -> None:
        super().__init__()
        self.engine = pyttsx3.init()

        self.engine.setProperty('rate', 205)
        self.engine.setProperty('volume', 1)

        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[7].id) #voices index 7 represesnts a british male voice, similar to JARVIS

    def speak(self, txt:str) -> None:
        '''
        Synthesizes speech based on given text

        :param txt: string of text to speechify
        '''
        self.engine.say(txt)
        self.engine.runAndWait()

    def greet_user(self) -> None:
        """
        Greets user according to time of day (morning, afternoon, evening)
        """
        current_time = datetime.now()
        current_hour = current_time.hour

        if current_hour >= 0 and current_hour < 12:
            self.speak(f"Good morning {USERNAME}")
        elif current_hour >= 12 and current_hour < 18:
            self.speak(f"Good afternoon {USERNAME}")
        elif current_hour >= 18 and current_hour < 24:
            self.speak(f"Good evening {USERNAME}")
        self.speak(f"I am {BOTNAME}. How may I assist you?")

    def listen(self) -> str:
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
                self.speak(query)
                self.speak(choice(performing_task))
            else:
                hour = datetime.now().hour
                if hour >= 21 and hour < 6:
                    self.speak("Good night sir, take care!")
                else:
                    self.speak('Have a good day sir!')
                exit()
        except Exception:
            self.speak('Sorry, I could not understand. Could you please say that again?')
            query = 'None'
        return query



# def main():
#     jarvis = Engine()
#     jarvis.speak("Initiating...")
#     jarvis.greet_user()
#     while True:
#         jarvis.listen()

# if __name__ == '__main__':
#     main()