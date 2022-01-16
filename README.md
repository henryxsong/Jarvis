# Greetings Sir/Ma'am, I am Jarvis. 
 
## Description

Okay, not the actual J.A.R.V.I.S made by Tony Stark, but a simplified version of it. Somewhere along my family tree are my more famous cousins Siri and Alexa.

As huge fan of the MCU, I drew inspiration from Tony Stark's arsenal of technology. While I may not have the ability to build a functional Iron Man suit (yet), it is within my skillset to build Jarvis, ableit an extremely simplified version. Unfortunately, I cannot change nuclear launch codes as seen in Avengers: Rise of Ultron.

It is designed to act as a voice assistant on your computer, capable of performing simple tasks. Current planned capabilities are found below in the ToDo section, but more may be added in the future.  

## Usage
1. Clone the repo
```
    git clone https://github.com/henryxsong/Jarvis.git
```

2. Navigate to the root directory of the repo

3. Install dependencies
```
    pip install -r requirements.txt
```

4. Run program
```
    python3 Jarvis.py
```

## To Do
- [x] Create speech engine
- [x] Create listener to listen to user voice commands
- [x] Perform simple information retrieval tasks (i.e. weather, time, location, etc)
- [x] Perform non-intrusive tasks on local machine (i.e. open/close application)
- [ ] Expand database of phrases
- [ ] Expand compatibility with Windows
- [ ] Implement Docker (or create executable package)
- [ ] Implement a front-end interface (i.e. a synthesizer like hal in 2001: A space odyssey)
- [ ] Obtain the mind stone to make Jarvis sentient

## Dependencies
| Package | Version |
| ----------- | ----------- |
| Python | 3.0+ |
| psutil | 5.8.0 |
| python-decouple | 3.5 |
| pyttsx3 | 2.9 |
| pywhatkit | 5.2 |
| requests | 2.26.0 |
| wikipedia | 1.4.0 |
| PyAudio | n/a |
| SpeechRecognition | 3.8.1 |



## Compatibility
Currently designed and tested for MacOS (12.1) using Python3 (3.9.1).

## Privacy
This program, by default, will utilize your computer's microphone and will listen to audio picked up by your system's micophone. In the script that I have written, no part of the program stores/logs/sends recordings with one exception. Only the latest voice command will be stored in a variable as a string of text to be parsed and run, but once a new command is given, the old command will be overwritten. This utilizes the python packages pyttsx3 and speech_recognition, which to my knowledge, does not store/log data. Feel free to browse the source code to verify :)

Your IP address is utilized for determining your location. It is stored in a local variable when the program is running, and is used in API calls to obtain weather and location information, but no data is sent to the server.
