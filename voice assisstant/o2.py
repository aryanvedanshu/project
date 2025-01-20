import pyttsx3 as p
import speech_recognition as sr
from yt_play import youtube
from wiki import infow

engine = p.init()

rate = engine.getProperty('rate')
print (rate)

