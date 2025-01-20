import pyttsx3 as p
import speech_recognition as sr
from yt_play import youtube
from wiki import infow
from google import goog
import randfacts as rdf
from bs4 import BeautifulSoup
import os
import webbrowser
import datetime
import operator
import random
import wolframalpha
#import JSON
import win32com.client as wincl
from urllib.request import urlopen
from ecapture import ecapture as ec
from PyPDF2 import PdfReader
import os
from jokes import *

engine = p.init()

rate = engine.getProperty('rate')
#print (rate)

rate = engine.setProperty('rate', 240)
#print (rate)

voice = engine.getProperty('voices') #get the available voices
# engine.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
engine.setProperty('voice', voice[1].id) #changing voice to index 1 for female voice
    
"""
engine.say("I am vengence .I am the Knight. I! AM! BATMAN!!")
engine.runAndWait()
"""
def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")

    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")   

    else:
        speak("Good Evening Sir !")  

    assname =("Jarvis 1.o")
    speak("I am your Assistant")
    speak(assname)
    
wishMe()

def takeCommand():
    
    r = sr.Recognizer()
        
    with sr.Microphone(device_index=1) as source:
            
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language ='en')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Unable to Recognize your voice.")  
        return None
        
    return query
    
def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    
    print("#####################")
    print("Welcome Mr.", uname)
    print("#####################")
    
""" username()
text = takeCommand()
 """

# Use the default system microphone as the source
""" with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Say something now")
    audio = r.listen(source)
    text=r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("What its not like I care for you or anything?")
speak("Just tell.") """

""" if "How" and "are" and "you" in text:
    speak("What its not like I care for you or anything?")
 """
""" speak(datetime.datetime.now())
speak("Tell Me website you want to access")
 """
google=['google','Google']
text2=takeCommand()
print(text2)
match(text2):
    case ("Wiki"):
        speak("topic please?")
        wiki=takeCommand()
        print(wiki)
        # Create an instance of the infow class
        assist = infow()
        # Call the get_info method with the query "info"
        assist.get_info(wiki)
        input("Press Enter to exit...")
        
    case ("video"):
        speak("name please?")
        video=takeCommand()
        print(video)
        # Create an instance of the youtube class
        play_vid = youtube()
        play_vid.play(video)
        input("Press Enter to exit...")
        
    case "google" | "Google":
        speak("topic please?")
        google=takeCommand()
        print(google)
        # Create an instance of the goog class
        assist = goog()
        # Call the google_search method with the query "goog"
        assist.google_search(google)
        input("Press Enter to exit...")
        
    case ("fact"):
        speak("Ok How about this")
        x = rdf.getFact()
        speak("Did you know that, " + x)
        print("Did you know that, " + x)

    case ("joke"):
        speak("Ok How about this")
        arr = joke()
        print(arr[0])
        speak(arr[0])
        print(arr[1])
        speak(arr[1])
        
    case _:
        speak("I cant do that")