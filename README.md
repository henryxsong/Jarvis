# Greetings Sir/Ma'am, I am Jarvis. 
 
## Description

Okay, not the actual J.A.R.V.I.S made by Tony Stark, but a simplified version of it. Somewhere along my family tree are my more famous cousins Siri and Alexa.

As huge fan of the MCU, I drew inspiration from Tony Stark's arsenal of technology. While I may not have the ability to build a functional Iron Man suit (yet), it is within my skillset to build Jarvis, ableit an extremely simplified version. Unfortunately, I cannot change nuclear launch codes as seen in Avengers: Rise of Ultron.

It is designed to act as a voice assistant on your computer, capable of performing simple tasks. Current planned capabilities are found below in the ToDo section, but more may be added in the future.  

## ToDo
- [x] Create speech engine
- [x] Create listener to listen to user voice commands
- [ ] Perform simple information retrieval tasks (i.e. weather, time, location, etc)
- [ ] Perform non-intrusive tasks on local machine (i.e. open application, play music, etc)
- [ ] Expand database of phrases
- [ ] Implement Docker (? tbd)
- [ ] Implement a front-end interface (i.e. a synthesizer like hal in 2001: A space odyssey)
- [ ] Obtain the mind stone to make Jarvis sentient


## Compatibility
Currently designed and tested for MacOS (12.1) using Python3 (3.9.1).

## Privacy
This program, by default, will utilize your computer's microphone and will listen to audio picked up by your system's micophone. In the script that I have written, no part of the program stores/logs/sends recordings with one exception. Only the latest voice command will be stored in a variable as a string of text to be parsed and run, but once a new command is given, the old command will be overwritten. This utilizes the python packages pyttsx3 and speech_recognition, which to my knowledge, does not store/log data. Feel free to browse the source code to verify :)
