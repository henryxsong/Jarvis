import Engine

class Jarvis(object):
    def __init__(self) -> None:
        super().__init__()
        self.jarvis = Engine.Engine()
        self.run()
    
    def run(self):
        self.jarvis.speak("Initiating...")
        self.jarvis.greet_user()
        while True:
            self.jarvis.listen()

if __name__ == '__main__':
    Jarvis()

    