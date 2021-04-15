#MMM-H.I.V.E V.0.0.1 BETA  : Home-Assistant Intergrated Virtual Environment
# #VIEW THE HIVE PROJECT AT HTTPS://natebrownprojects.github.io/TheHiveProject/
# Copyright: Nate Brown Projects 2021 / Nate Brown 2021 / TheHiveProjectNZ 2021
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import math
from datetime import timedelta
import wikipedia
import pyjokes
import json
from pyttsx3 import Engine
import requests
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import wx


listener = sr.Recognizer()
engine: Engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0]  .id)

## DO NOT EDIT!!! ---------
def talk(text):
    engine.say(text)
    engine.runAndWait()
talk('Systems Loading, Welcome to the HIVE.')
talk('How, can i help, you Sir?')
print('Communication Log:')




## WEATHER CONFIG BELOW:






def newweather():
    owm = OWM('c315355b9f2f252cf5dbab09eff036ae')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Auckland,NZ')
    w = observation.weather
    talk(w.detailed_status)
    pass
def currentw():
    owm = OWM('c315355b9f2f252cf5dbab09eff036ae')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Auckland,NZ')
    w = observation.weather
    print(w.detailed_status)
    talk('The current conditions in Auckland:' + w.detailed_status)
    pass
def windw():
    owm = OWM('c315355b9f2f252cf5dbab09eff036ae')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Auckland,NZ')
    w = observation.weather
    print(w.wind())
    pass

def tempw():
    owm = OWM('c315355b9f2f252cf5dbab09eff036ae')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Auckland,NZ')
    w = observation.weather
    print(w.temperature)
    talk(w.temperature('celsius'))

def cloudw():
    owm = OWM('c315355b9f2f252cf5dbab09eff036ae')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Auckland,NZ')
    w = observation.weather
    print(w.clouds)
    talk(w.clouds)
    pass

def rain():
    owm = OWM('c315355b9f2f252cf5dbab09eff036ae')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Auckland,NZ')
    w = observation.weather
    print(w.rain)
    talk(w.rain)
    pass



## END OF WEATHER CONFIG


def take_command():
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hive' in command:
                command = command.replace('hive', '')
                print('Command: ' + command)

    except:
        pass

    return command

def run_hive():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'date' in command:
        now = datetime.datetime.now()
        talk("Current date and time : ")
        talk(now.strftime("%d         %m                %Y"))
        engine.setProperty("rate", 178)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1, auto_suggest=False)
        print(info)
        talk(info)
    elif 'what is pi' in command:
        print(math.pi)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open project 65' in command:
        talk('Access Denied')
    elif 'hi' in command:
        talk('Hello, How are you?')
       




    ## WEATHER CONFIG COMMANDS

    elif 'current weather' in command:
        newweather()
    elif 'current wind' in command:
        windw()
    elif 'current rain' in command:
        rainw()
    elif 'current temp' in command:
        tempw()
    elif 'cloud' in command:
        cloudw()

    ## END OF WEATHER CONFIG COMMANDS

    elif 'status report' in command:
        talk('All Systems Operational Sir!')
    elif 'hive' in command:
        talk('Yes, sir?')
    elif 'shut down' in command:
        talk('Shutting all Hive Systems Down.')
        talk('Thank you for using hive! Goodbye!')
        print('Thank you for using H.I.V.E!')
        exit()

    elif 'exit' in command:
        talk('Shutting all Hive Systems Down.')
        talk('Thank you for using hive! Goodbye!')
        print('Thank you for using H.I.V.E!')
        exit()
    elif 'awesome thanks' in command:
        talk('Your, Welcome!')
    elif 'thanks' in command:
        talk('Ny Pleasure!')
    elif 'thank you' in command:
        talk('No Problem!')
    elif 'awesome' in command:
        talk('No Problem, is there anything i, can help you, with?')
    elif ' no' in command:
         talk('ok!')
    elif 'yes' in command:
        talk('Ok, what is it?')
    elif 'how are you' in command:
        talk('I am Great! ,, How are you!?')
        har = input('How are you?: ')
        print('Thats Good!')

    elif 'you still there' in command:
        talk('Yes Sir, i am ready for your command!')
    elif 'who are you' in command:
        talk('My name is Hive. It stands for Home Assistant Intergrated Virtual Environment. I am here to help you with whatever i can')
    elif 'hello' in command:
        talk('hello, how are you today?')
    elif 'version' in command:
        talk('I am currently running on Version 0.0.1 BETA as of Thursday April 15th 5:49PM')
    else:
        print('Please say the command again.')
        talk('Invalid Command!')
        input('Please Type Your Command: ')
        take_command()


while True:
    try:
        run_hive()
    except UnboundLocalError:
        talk('An Error has occurred, Please reload the System. If this error continues please open an issue on Github.com/NateBrownProjects/TheHiveProject/Issues.')
        print('An Error has occurred, Please reload the System. If this error continues please open an issue on Github.com/NateBrownProjects/TheHiveProject/Issues.')
        continue
