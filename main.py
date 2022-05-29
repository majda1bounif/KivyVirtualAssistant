import pprint
import re
import time
import webbrowser

import kivy
import requests

import loc
import wolframalpha as wolframalpha
import google_calendar
import news
import send_mail
import pyttsx3 as pyttsx3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import playsound
import pyjokes
import news
import wikipedia
import pyaudio
import pywhatkit
import pyttsx3
import random
import date_time
from kivymd.uix.screen import MDScreen
from pyttsx3 import voice
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import speech_recognition as sr
kivy.require('2.1.0')
import system_stats
import weather
global engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
r = sr.Recognizer()
langswitch = "en"
htext = "a"
greetings = ['hello boss', 'how can I help you?', 'I am all ears', 'yes boss']
EMAIL_DIC = {
    'husband': 'benmyrat@gmail.com',
    'myself': 'naima1benhadia@gmail.com',
    'my official email': 'majda1bounif@gmail.com',
    'my second email': 'majda1bounif@gmail.com',
    'my official mail': 'majda1bounif@gmail.com',
    'my second mail': 'majda1bounif@gmail.com'
}
client = wolframalpha.Client('JUAEY3-LP333PH42K')


def speak(text):
    engine.say(text)
    engine.runAndWait()
def google_calendar_events(text):
    service = google_calendar.authenticate_google()
    date = google_calendar.get_date(text)


def computational_intelligence(question):
    try:
        client = wolframalpha.Client('JUAEY3-LP333PH42K')
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None


class Main(Screen):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.name="Main"
    def on_enter(self, *args):
        wish()
    def start_listening(self):
        with sr.Microphone() as source:
            r.pause_threshold = 0.7
            r.adjust_for_ambient_noise(source)
            print("listennig...")
            audio = r.listen(source)
            print("recognition")
            voice = ""

        try:
            voice = r.recognize_google(audio, language="EN-en")
        except sr.UnknownValueError:
            print("system unknown value error--> sentence is not understanding")
        except sr.RequestError:
            print("system request error")
        print(voice)
        return voice

    def commands(self):
        try:
            cmd = self.start_listening().lower()
        except:
            print('something went wrong')
        if cmd == 'hello' or cmd == 'halo' or cmd == 'hi':
            speak(random.choice(greetings))
        elif cmd == 'time' or cmd == 'sime' or cmd == 'sign':
            c_time = date_time.time()
            speak(f"Currently it is {c_time}")
        elif cmd == 'date' or cmd == 'dates':
            c_date = date_time.date()
            speak(f"Today is {c_date}")
        elif 'youtube' in cmd:
            video = cmd.replace('YouTube', '')
            speak(f"Okay , playing {video} on youtube")
            pywhatkit.playonyt(video)
        elif re.search('weather', cmd):
            city = cmd.split(' ')[-1]
            weather_res = weather.fetch_weather(city=city)
            speak(weather_res)
        elif 'send email' in cmd or 'email' in cmd:
            sender_email = 'salmaettaibi28@gmail.com'
            sender_password = 'kimkai1998'
            try:
                speak('whom do you want email ?')
                recipient = self.start_listening()
                receiver_email = EMAIL_DIC.get(recipient)
                if receiver_email:
                    speak('What is the subject ?')
                    subject = self.start_listening()
                    speak('what should I say ?')
                    message = self.start_listening()
                    msg = 'Subject: {}\n\n{}'.format(subject, message)
                    send_mail.mail(sender_email, sender_password, receiver_email, msg)
                    speak("Email has been successfully sent")
                    time.sleep(2)
                else:
                    speak("I coudn't find the requested person's email in my database. Please try again with a "
                          "different name")
            except:
                speak("Sorry Majda. Couldn't send your mail. Please try again")
        elif "calculate" in cmd:
            question = cmd
            answer = computational_intelligence(question)
            speak(answer)
        elif "buzzing" in cmd or "news" in cmd or "headlines" in cmd:
            news_res = news.get_news()
            speak('Source: The Times Of Russia')
            speak('Todays Headlines are..')
            for index, articles in enumerate(news_res):
                pprint.pprint(articles['title'])
                speak(articles['title'])
                if index == len(news_res) - 2:
                    break
            speak('These were the top headlines, Have a nice day Boss!!..')
        elif "joke" in cmd or "jokes" in cmd:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        elif "where is" in cmd:
            place = cmd.split('where is ', 1)[1]
            current_loc, target_loc, distance = loc.loc(place)
            city = target_loc.get('city', '')
            state = target_loc.get('state', '')
            country = target_loc.get('country', '')
            time.sleep(1)
            try:
                if city:
                    res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                    print(res)
                    speak(res)

                else:
                    res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                    print(res)
                    speak(res)

            except:
                res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
                speak(res)
        elif "my location" in cmd or "location" in cmd:
            city, state, country = loc.my_location()
            res = f"currently you are in {city} state of {state} country{country}"
            speak(res)
        elif "system" in cmd or "info" in cmd:
            res =system_stats.system_stats()
            speak(res)
        elif "IP address" in cmd or 'address' in cmd:
            ip = requests.get('https://api.ipify.org').text
            print(ip)
            speak(f"Your ip address is {ip}")
        elif "close" in cmd:
            engine.stop()






















        else:
            cmd = cmd
            speak('let me think...')
            try:
                try:
                    res = client.query(cmd)
                    results = next(res.results).text
                    # speak('WOLFRAM-ALPHA says - ')
                    speak('OK Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(cmd, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')
        speak('Next Command Boss!')


sm = ScreenManager()
screen = Screen(name='Main')
sm.add_widget(screen)


class MainApp(MDApp):
    def build(self):
        self.title = 'KivyMD Dashboard'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_file('main.kv')



MainApp().run()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Jarvis. Online and ready Boss. Please tell me how may I help you")
