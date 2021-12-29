
from math import trunc
from subprocess import check_output
import pyttsx3
import numpy as np
import cv2
from moviepy.editor import *
from twilio.rest import Client
from state import state
import imutils
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import pyowm
import time
import cv2
import os
import speedtest
import turtle
import time
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import psutil
import pyperclip
import webbrowser
import smtplib
import pyautogui
import random
import speech_recognition as sr
import wikipedia
import socket
from requests import get
import datetime
import wolframalpha
import pyautogui as pg
from os import environ, stat
import os
import sys
from tqdm import tqdm
from time import sleep
import pywhatkit as kit
import os.path
import cv2
from bs4 import BeautifulSoup
import requests
import socket as s
from pywikihow import search_wikihow
from pynput.keyboard import Key, Controller
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from pytube.cli import on_progress
from pytube import YouTube
import os
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import pyttsx3





engine = pyttsx3.init('sapi5')

voice = engine.getProperty('voices')

def ProgressBar():
    for i in tqdm(range(5)):
        sleep(0.9)

name="Rahul"
city="Indore"
age="14"
gender="Sir"
URL = "https://news.google.com/rss"
URL1 = 'https://feeds.feedburner.com/ndtvnews-top-stories'
URL2 = 'https://www.aajtak.in/rssfeeds?id=home'




engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('R7A69X-LQE32TVWX7')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-3    ].id)


def speak(audio):
    print('ULTRON: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def Tic():
    print(Start)

def translator():
    speak("ok sir give some information to do this")
    speak("What is language in which you are speaking for example english,hindi")
    origin = str(input("Enter Here: "))
    speak("Language to translate")
    final = str(input("Enter Here: "))
    speak("Text to translate")
    text = myCommand()
    langs = Translator(from_lang = f"{origin}",lo_lang=f"{final}")
    translate = langs.trans(f"{text}")
    print(translate)

def AddContact():
        speak(f'Boss, Enter the contact details')
        name = input("Enter the name :").lower()
        number = input("Enter the number :")
        NumberFormat = f'"{name}":"+91{number}"'
        ContFile = open("Contacts.txt", "a") 
        ContFile.write(f"{NumberFormat}\n")
        ContFile.close()
        speak(f'Boss, Contact Saved Successfully')

def SearchCont():
        with open("Contacts.txt","r") as ContactsFile:
            for line in ContactsFile:
                if name in line:
                    speak("Name Match Found")
                    s = line.split("\"")
                    return s[1],s[3],True
        return 0,0,False

    
def Display():
        ContactsFile = open("Contacts.txt","r")
        count=0
        for line in ContactsFile:
            count+=1
        ContactsFile.close()
        ContactsFile = open("Contacts.txt","r")
        speak(f"Boss displaying the {count} contacts stored in our data base")    
        for line in ContactsFile:
            s = line.split("\"")
            print("Name: "+s[1])
            print("Number: "+s[3])
        ContactsFile.close()



def googlenews():
    CLIENT = urlopen(URL)
    XML_PAGE = CLIENT.read()
    soup_page= soup(XML_PAGE,"xml")
    news_list = soup_page.findAll("item")
    for news in news_list:
        speak(news.title.text)
        speak(news.pubDate.text)
        print('-'*60)

def QrCodeScanner():
    i = 0
    cap = cv2.VideoCapture(0)
    while i<4:
        _,frame = cap.read()
        decoded = pyzbar.decode(frame)
        for obj in decoded:
            print(obj.data)
            i = i+1
        cv2.imshow("QRCode",frame)
        cv2.waitKey(5)
        cv2.destroyAllWindows
def NdtvNews():
    
    CLIENT = urlopen(URL1)
    
    XML_PAGE = CLIENT.read()
    soup_page= soup(XML_PAGE,"xml")
    news_list = soup_page.findAll("item")
    for news in news_list:
        print(news.title.text)
        speak(news.title.text)
        print('-'*10)

def SMS():
    account_sid = 'ACd103ec0159b799046b1ad06d893ebc70'
    auth_token = 'ae4f9370d2454d3595a3cea00482c1d2'
    
    client = Client(account_sid, auth_token)
    client.api.account.messages.create(
        print("enter the number to sent message"),
        to=int(input()),
        from_="+12168687392",
        body="Hello there!")


def news():
    """
    This method will tells top 15 current NEWS
    :return: list / bool
    """
    try:
        news_url = "https://news.google.com/news/rss"
        Client = urlopen(news_url)
        xml_page = Client.read()
        Client.close()
        soup_page = soup(xml_page, "xml")
        news_list = soup_page.findAll("item")
        li = []
        for news in news_list[:15]:
            li.append(str(news.title.text.encode('utf-8'))[1:])
        return li
    except Exception as e:
        print(e)
        return False



def AjaTak():
    
    CLIENT = urlopen(URL2)
    
    XML_PAGE = CLIENT.read()
    soup_page= soup(XML_PAGE,"xml")
    news_list = soup_page.findAll("item")
    for news in news_list:
        print(news.title.text)
        speak(news.description.text)
        print('-'*10)

def VideoEditor():
    location = int(input("Enter the location of video:"))
    Rotation = int(input("Enter how much degree You want to rotat video:"))
    clip = VideoFileClip(f"{location}").rotate(Rotation)
    clip.python_display(width=280)


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')
        

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

def shedule(self):
        day = self.Cal_day().lower()
        self.talk("Boss today's shedule is")
        Week = {"monday" : "Boss from 9:00 to 9:50 you have Hindi Class, from 9:50 to 11:50 you have mechanics class, from 12:00 to 2:00 you have brake, and today you have sensors lab from 2:00",
        "tuesday" : "Boss from 9:00 to 9:50 you have English class, from 10:00 to 10:50 you have break,from 11:00 to 12:50 you have ELectrical class, from 1:00 to 2:00 you have brake, and today you have biology lab from 2:00",
        "wednesday" : "Boss today you have a full day of classes from 9:00 to 10:50 you have Data structures class, from 11:00 to 11:50 you have mechanics class, from 12:00 to 12:50 you have cultural class, from 1:00 to 2:00 you have brake, and today you have Data structures lab from 2:00",
        "thrusday" : "Boss today you have a full day of classes from 9:00 to 10:50 you have Maths class, from 11:00 to 12:50 you have sensors class, from 1:00 to 2:00 you have brake, and today you have english lab from 2:00",
        "friday" : "Boss today you have a full day of classes from 9:00 to 9:50 you have Biology class, from 10:00 to 10:50 you have data structures class, from 11:00 to 12:50 you have Elements of computing class, from 1:00 to 2:00 you have brake, and today you have Electronics lab from 2:00",
        "saturday" : "Boss today you have a full day of classes from 9:00 to 11:50 you have maths lab, from 12:00 to 12:50 you have english class, from 1:00 to 2:00 you have brake, and today you have elements of computing lab from 2:00",
        "sunday":"Boss today is holiday but we can't say anything when they will bomb with any assisgnments"}
        if day in Week.keys():
            self.talk(Week[day])
def InternetSpeed():
        speak("Wait a few seconds boss, checking your internet speed")
        st = speedtest.Speedtest()
        dl = st.download()
        dl = dl/(1000000) #converting bytes to megabytes
        up = st.upload()
        up = up/(1000000)
        speak(f"Boss, we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")
def VideoTextAdder():
    location = input("Enter The location of video:")
    text = input("Enter the text to add on Video:")
    fontsize = input("Enter font size:")
    color = input("Enter the color of text:")
    Position = input("Enter The position of text ex bottom left right etc:")
    duration = input("Enter Duration Of video:")
    FPS = input("Enter The FPS:")
    videofilename = input("Enter The name of output file:")
    video = VideoFileClip(f"{location}").subclip(50,60)
    txt_clip = ( TextClip(f"{text}",fontsize=fontsize,color=f'{color}')
             .set_position(f'{Position}')
             .set_duration(duration) )

    result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
    result.write_videofile(f"{videofilename}",fps=300)


def myCommand():
   
   
    r = sr.Recognizer()                                                                                  
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except Exception as e:
        speak('say again sure i will do it')
        query = myCommand()
    query = query.lower()
    return query


def read():
    pg.hotkey("ctrl",'c')
    tobespoken=pyperclip.paste()
    speak(tobespoken)

def spotify():
    speak("speak the song which you want to play")
    search = myCommand()
    url = "https://open.spotify.com/search/"
    speak(f"you said to play {search}")
    webbrowser.open(f'https://open.spotify.com/search/{search}')



def Covid(s):
        try:
            from covid_india import states
            details = states.getdata()
            if "check in" in s:
                s = s.replace("check in","").strip()
                print(s)
            elif "check" in s:
                s = s.replace("check","").strip()
                print(s)
            elif "tech" in s:
                s = s.replace("tech","").strip()
            s = state[s]
            ss = details[s]
            Total = ss["Total"]
            Active = ss["Active"]
            Cured = ss["Cured"]
            Death = ss["Death"]
            print(f"Boss the total cases in {s} are {Total}, the number of active cases are {Active}, and {Cured} people cured, and {Death} people are death")
            speak(f"Boss the total cases in {s} are {Total}, the number of active cases are {Active}, and {Cured} people cured, and {Death} people are death")
            time.sleep(5)
            speak("Boss do you want any information of other states")
            I = myCommand()
            print(I)
            if ("check" in I):
                Covid(I)
            elif("no" in I):
                speak("Okay boss stay home stay safe")
            else:
                speak("Okay boss stay home stay safe")
        except:
            speak("Boss some error occured, please try again")
            speak("Boss do you want any information of other states")
            I = myCommand
            if("yes" in I):
                speak("boss, Which state covid status do u want to check")
                Sta = myCommand
                Covid(Sta)
            elif("no" in I):
                speak("Okay boss stay home stay safe")

def condition():
        usage = str(psutil.cpu_percent())
        speak("CPU is at"+usage+" percentage")
        battray = psutil.sensors_battery()
        percentage = battray.percent
        speak(f"Boss our system have {percentage} percentage Battery")
        if percentage >=75:
            speak(f"Boss we could have enough charging to continue our work")
        elif percentage >=40 and percentage <=75:
            speak(f"Boss we should connect out system to charging point to charge our battery")
        elif percentage >=15 and percentage <=30:
            speak(f"Boss we don't have enough power to work, please connect to charging")
        else:
            speak(f"Boss we have very low power, please connect to charging otherwise the system will shutdown very soon")



greetMe()
speak("Initialising system")
speak("Security Check is going on")
speak('Hello Boss, I am your digital ULTRON')
speak('i will Work always for you')

  
if __name__ == "__main__":
        
    

    while True:   
    
            query = myCommand();
            query = query.lower()
        
            if 'open youtube' in query:
                speak('okay')
                webbrowser.open('www.youtube.com')

            if "Game" in query:
                Tic()

            if "read" in query:
                try:
                    read()
                except:
                   speak("no query selected plz select a query")
            if "Covid" or "Corona" in query:
                Covid()
            if "check Net speed" or "Speed of net"  in query:
                InternetSpeed()
            if "Condition of our system" or "System condition" in query:
                speak("checking the condition of system Boss")
                condition()

            if "translate this" in query:
                translator()
 
            if "news from google" in query:
                googlenews() 

            if "news from ndtv" in query:
                NdtvNews()

            if "news from home" in query:
                AjaTak()
            

                
                
                

            


            if"say something" in query:
                speak("what's your name?")

            if "mask" in query:
                os.system("python MaskDetector.py")
                
            if "who created you" in query:
                speak("I was created by Rahul on 12 of april on 2020")

            if "who made you" in query:
                speak(" was created by Rahul on 12 of april on 2020")

            if "hack" in query:
                wifi()

            if "who is Rahul" in query:
                speak("Rahul is my developer my teacher the one who taught me how be a good wise smart and a intelligent person HELEN was previously his name And since he left the hacking world he gave this name to me and started programming with python then created me  Now i Am proud to be Helen at last ")

            if "how were you developed" in query:
                speak("Sorry boss  I am not allowed to reveval all my secrets  ")

            if "how is weather" in query:
                city=(f"{city}")
                get()


            if "how are you developed" in query:
                speak("Sorry boss  I am not allowed to reveval all of my secrets  ")

            if "select all" in query:
                pg.hotkey('ctrl','a')

            if "close this window" in query:
                pg.hotkey('alt','f4')

            if "open a new tab" in query:
                pg.hotkey('ctrl','n')

            if "open a new incognito window" in query:
                pg.hotkey('ctrl','shift','n')

            if "copy" in query:
                pg.hotkey('ctrl','c')
                speak('query copied to clipboard')

            if "paste" in query:
                pg.hotkey('ctrl','v')

            if "undo" in query:
                pg.hotkey('ctrl','z')

            if "redo" in query:
                pg.hotkey('ctrl',)

            if "save" in query:
                pg.hotkey('ctrl','s')

            if "back" in query:
                pg.hotkey('browserback')

            if "open mask" in query:
                done = dmv.open_camera()
                if done == 1:
                    speak("mask detection done")


            if "go up" in query:
                pg.hotkey('pageup') 

            if "go to top" in query:
                        pg.hotkey('home')

            elif "Introduce yourself" in query:
                speak("Okay,Let me start by The time I was born,,")
                speak("I was a dream of a boy dreaming to make a perfect virtual assistant")
                speak("He soon established the company named ROGER industries")
                speak("Slowly,I came to life")
                speak("I started learning various things like calculations,General knowldge etc etc")
                speak("Now I am capable of doing various things like Beatboxing,opening applications,Cracking jokes,Playing music etc.")
                speak("Okay,thats a wrap I wont say more ")

            elif 'battery left' in query or 'how much power left' in query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"sir our system have {percentage} percent battery")

            elif 'you are not bored' in query:
                speak("no i am not bored because i am moving all around the internet ")
                
            elif 'search this on brainly' in query:
                search = myCommand()
                url = 'https://brainly.in/app/ask?entry=hero&q='
                speak("you said me to search" +search)
                speak("ok sir opening")
                webbrowser.open(f"https://brainly.in/app/ask?entry=hero&q={search}")



            elif "play iron man 1" in query:
                speak("ok sir")
                webbrowser.open("https://www.hotstar.com/in/movies/iron-man/1660000038/watch")

            elif "play songs" in query:
                speak("speak the song name")
                songname = myCommand()
                kit.playonyt(f"{songname}")

            elif "play iron man 2" in query:
                speak("ok sir")
                webbrowser.open("https://www.hotstar.com/in/movies/iron-man-2/1660000039/watch")

            elif "play iron man 3" in query:
                speak("ok sir")
                webbrowser.open("https://www.hotstar.com/in/movies/iron-man-3/1660000042/watch")

            elif "i want to see movie" in query:
                url = 'https://www.hotstar.com/in/search?q='
                name = myCommand()
                speak(f"As you said {name}")
                speak(f"wait sir i am serching the movie{name}")
                webbrowser.open(f"https://www.hotstar.com/in/search?q={name}")
                speak("enjoy the movie sir")

            elif "close" in query:
                program = myCommand()
                speak(f"okay sir, closing {program}")
                os.system(f"taskkill /f /im {program}.exe")

            elif "set alarm" in query:

                nn = int(datetime.datetime.now().hour)
                if nn==22: 
                    music_dir = 'D:\\Songs'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))
                

            elif 'download the video' in query:
                speak("ok sir you have to put the link of the video")
                video_url = input("sir paste the link here :")
                print("\n")
                try:
                     yt = YouTube(video_url, on_progress_callback=on_progress)
                     yt.streams\
                        .filter(file_extension='mp4')\
                        .get_highest_resolution()\
                        .download()

                except EOFError as err:
                    print(err)
    
                
                else:
                    speak("i have downloaded the video sir you can check in the directory where i am store")
            


            elif "lot" in query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

                


            elif "you are the best" in query:
                speak("thank you boss")

            elif "class of vedantu on monday" in query:
                webbrowser.open()

            elif "who made you" in query:
                speak("i was just a idea and rahul gave me birth and i am here taking to you")

            elif "what is the meaning of plato" in query:
                speak("P.L.A.T.O.:- P.L.A.T.O. also called Piezo-electrical Logistic Analytical Tactical")

            elif "activate youtube mode" in query:
                speak("what do you want to search")
                search = myCommand()
                url = 'https://www.youtube.com/results?search_query='
                speak("ok sir")
                webbrowser.open(f'https://www.youtube.com/results?search_query={search}')

            elif "track the number" in query:
                speak("Enter the number to get the location")
                L = input()
                phone_number  = phonenumbers.parse(L)
                speak(geocoder.description_for_number(phone_number,"en"))
                speak(carrier.name_for_number(phone_number ,"en"))

            elif "contact" in query or "search this contact" in query:
                D1={}
                while True:
                    n=int(input("ENTER THE NUMBER TO STORE[0/1/2]:-"))
                    if n==1:
                        name = input("ENTER NAME--")
                        phnu = int(input("ENTER PHONE NUMBER"))
                        D1[name]=phnu
                    
                    elif n==2:
                        name1=input("enter name to search the contact")
                        speak("contact number of",name1,"is",D1[name1])

                    elif n==3:
                        break



            elif "search this person on facebook" in query:
                search = myCommand()
                url = 'https://www.facebook.com/search/top?q='
                speak(f"you said to search for"+search)
                webbrowser.open(f'https://www.facebook.com/search/top?q={search}')

            elif "search this on amazon" in query:
                search = myCommand()
                url = 'https://www.amazon.in/s?k='
                speak(f"you said me to search"+search)
                webbrowser.open(f"https://www.amazon.in/s?k={search}")

            elif "standby mode" in query:
                speak("ok boss you can call me any time just say the hotword")

            elif "sleep now " in query:
                speak("i am slepping you can call me anytime")
                break
                


            elif 'Which company info do you have ' in query:
                speak("rahul is building the comapny it will take 2 years to build")

            elif 'send message to group' in query:
                speak("yes sir")
                message = myCommand()
                speak("enter time in 24 hours format like 24 09")
                kit.sendwhatmsg_to_group('https://web.whatsapp.com/accept?code=https://chat.whatsapp.com/J3svwINW6Wp3Osz1ZlG5WK',f'{message}',int(input()),int(input()))
                speak("message send boss")

            

                
            elif "draw triangle" in query:
                speak("here is your trangle sir")
                
                def form_tri(side): 
                    for i in range(3): 
                        my_pen.fd(side) 
                        my_pen.left(120) 
                        side -= 2
                
                        

                tut = turtle.Screen() 
                tut.bgcolor("green") 
                tut.title("TRIANGLE") 
                
                my_pen = turtle.Turtle() 
                my_pen.color("orange") 
                
                tut = turtle.Screen()            
                

                side = 300
                for i in range(1): 
                    form_tri(side) 
                    side -= 1
                    break

            elif "shut down my laptop" in query:
                shutdown = speak("if you want to shutdown your laptop say yes or no sir")
                if shutdown == 'no': 
                    exit()
                else: 
                    os.system("shutdown /s /t 1")

            elif "restart my laptop" in query:
                os.system("shutdown /r /t 1")

            elif "send whatsapp message to" in query:
                speak('what i have to send sir')
                say = myCommand()
                speak('enter the number to send message')
                phonenumber = int(input())
                speak('enter time in 24 hrs format like 23 04')
                kit.sendwhatmsg(f'+91{phonenumber}', f"{say}",int(input()),int(input()))
                speak('message sent sir')


            elif "remember that" in query:
                speak("what should i remember sir for you")
                data = myCommand()
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()

            elif "what i told you to remember" in query:
                remember = open('data.txt','r')
                speak("you said me to remember was"+remember.read())



            elif 'switch window'in query  or 'switch the tab'in query:
                pyautogui.hotkey('alt','tab')

            elif 'volume up' in query:
                pyautogui.hotkey('volumeup')

            

            elif 'volume down' in query:
                pyautogui.hotkey('volumedown')

            elif 'start recording' in query:
                pyautogui.hotkey('win','alt','r')

            elif 'take screenshot' in query:
                pyautogui.hotkey('win','alt','PrtSc')

            elif 'stop recording' in query:
                pyautogui.hotkey('win','alt','r')

            elif 'play avengers endgame' in query:
                webbrowser.open_new_tab('https://www.hotstar.com/in/movies/avengers-endgame/1260013556/watch')

            elif ('can you calculate') in query:
                def add(x, y):
                    return x + y
                def subtract(x, y):
                    return x - y
                def multiply(x, y):
                    return x * y
                def divide(x, y):
                    return x / y
                    
                speak("Select operation.")
                speak("1.Add")
                speak("2.Subtract")
                speak("3.Multiply")
                speak("4.Divide")

                while True:
        
                    myCommand = input("Enter choice(1/2/3/4): ")

                    if myCommand in ('1', '2', '3', '4'):
                        num1 = float(input("Enter first number: "))
                        num2 = float(input("Enter second number: "))

                        if myCommand == '1':
                            speak(num1, "+", num2, "=", add(num1, num2))

                        elif myCommand == '2':
                            speak(num1, "-", num2, "=", subtract(num1, num2))

                        elif myCommand == '3':
                            speak(num1, "*", num2, "=", multiply(num1, num2))

                        elif myCommand == '4':
                            speak(num1, "/", num2, "=", divide(num1, num2))
                        break
                    else:
                        speak("Invalid Input")








            
        


                
                

        

            elif 'open google' in query:
                speak('okay')

            elif "draw square" in query:
                speak("here is your square sir ")
                def form_sq(side):
                    for i in range(4): 
                        my_pen.fd(side) 
                        my_pen.left(90) 
                        side -= 1 

                tut = turtle.Screen() 
                tut.bgcolor("green") 
                tut.title("SQUARE") 

                my_pen = turtle.Turtle() 
                my_pen.color("orange")

                tut = turtle.Screen()

                side = 400

                for i in range(1): 
                    form_sq(side) 
                    side-= 4
                    break

            elif "draw hexagon" in query:
                def form_hex(side): 
                    for i in range(6): 
                        my_pen.fd(side) 
                        my_pen.left(300) 
                        side -= 2

                tut = turtle.Screen() 
                tut.bgcolor("green") 
                tut.title("HEXAGON") 

                my_pen = turtle.Turtle() 
                my_pen.color("orange") 
                tut = turtle.Screen() 

                side = 120
    
                for i in range(1): 
                    form_hex(side) 
                    side -= 5
                    break

            elif "draw star" in query:
                def form_hex(side): 
                    for i in range(5): 
                        my_pen.fd(side) 
                        my_pen.left(500) 
                        side -= 2

                tut = turtle.Screen() 
                tut.bgcolor("green") 
                tut.title("STAR") 

                my_pen = turtle.Turtle() 
                my_pen.color("orange")

                tut = turtle.Screen() 

                side = 120
    
                for i in range(1): 
                    form_hex(side) 
                    side -= 5
                    break
            

            elif 'what is the time now' in query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak('Current time is ' + time)

            elif "gmail password" in query:
                email = environ.get('MY_EMAIL')
                passwd = environ.get('MY_PASSWORD')
                password  = input("enter the password to now your email")
                if password == os.environ['password_rahul']:
                    speak('ACCESS GRANT')
                    speak(f"sir your email is {email} this and password is {passwd}")
                else:
                    speak("ACCESS DENIED")
                    speak("you are not Rahul i can not give you my sir information")

            elif "my account" in query:
                usename = environ.get('ICICIUSERNAME')
                passwd = environ.get('ICICI_PASSWD')
                password  = input("YOUR PASSWORD TO KNOW YOUR BANK DETAILS")
                if password == os.environ['password_rahul']:
                    speak('ACCESS GRANT')
                    speak(f"sir your Bank ID is {usename} this and password is {passwd}")
                else:
                    speak("ACCESS DENIED")
                    speak("you are not Rahul i can not give you my sir information")
                    sys.exit()
                


            elif "password open" in query:
                keyboard = Controller()
                password = environ.get('excel_password')
                passwd = input("enter the password to open the file")
                if passwd == os.environ['password_rahul']:
                    speak("ACCESS GRANT")
                    os.startfile("D:\\IMPORTANT.xlsx")
                    
            
                else:
                    speak("ACCESS DENIED")
                    speak("you are not Rahul i can not give you my sir information")


            

                

            elif "lock my laptop" in query:
                pyautogui.hotkey('win','L')

            elif 'who are you' in query:
                speak("I am HELEN")

            elif 'are you married' in query:
                speak('I very lucky i never have to share things')
            
            elif 'open command prompt' in query:
                os.system("start cmd")
            elif 'open ms team' in query:
                fpath = "C:\\Users\\ytgam\\AppData\\Local\Microsoft\\Teams\\current\\Teams.exe"
                os.startfile(fpath)

            elif 'classes on monday' in query:
                speak("wait sir let me check")
                speak("i got it")
                speak("on monday you have 3 classes social science at 12:15 to 12:55 then hindi at 1:05 to 1:45 then english 1:55 to 2:35")

            elif 'up up down down left right left right' in query:
                speak('Jarvis simple mode enable')
                                  
            elif 'open minecraft' in query:
                spath = "C:\\Users\\ytgam\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
                os.startfile(spath)
            elif 'open github' in query:
                speak('okay')
                webbrowser.open('https://github.com')
            elif 'open discord' in query:
                gpath = "C:\\Users\\ytgam\\AppData\\Local\\Discord\\app-0.0.309\\Discord.exe"
                os.startfile(gpath)
            elif 'open code ' in query:
                hpath = "C:\\Users\\ytgam\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(hpath)              
            elif 'open gmail' in query:
                speak('okay')
                webbrowser.open('www.gmail.com') 

            elif "activate how to do mode" in query:
                speak("sir Mode Activated")
                while True:
                    speak("Tell me what do to want to known")
                    how = myCommand()
                    max_result = 1
                    how_to = search_wikihow(how, max_result)
                    assert len(how_to)  == 1
                    how_to[0].print()
                    speak(how_to[0].summary)
                    if "exit" in how or "deactivate the mode" in how:
                        speak("done sir")
                        break
            
            elif 'Neha Kakkar' in query:
                speak('Listen the beatiful songs of neha and enjoy')
                webbrowser.open('https://www.youtube.com/watch?v=6wNFJIbTxNk&list=PLzH1hgHiJn51QoXy4JJoYPNJQ47BTIUIS')

            elif 'play hotstar special ops' in query:
                webbrowser.open('https://www.hotstar.com/in/tv/special-ops/1260022894/guide/1260023040')

                

            elif "type this" in query:
                speak("ok sir wait i will open the notepad for you")
                kpath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(kpath)
                keyboard = Controller()
                for char in myCommand():
                    keyboard.press(char)
                    keyboard.release(char)
                    time.sleep(0.12)

        

            elif "hindi" in query:
                webbrowser.open('https://www.successcds.net/Class9/hindi/dohe.html')

        

                    
            elif 'Tony' in query:
                speak('okay')
                webbrowser.open('https://www.youtube.com/watch?v=B_hbJRNInkA&list=PLIp5xbTZchwcVYXv27_KskTWY5XUrTWkl')       

            elif '9 month ki story' in query:
                speak('okay')
                webbrowser.open('https://www.sonyliv.com/shows/story-9-months-ki-1700000546')

            elif 'sleep now' in query:
                speak("ok sir i am sleeping you can call me anytime just say wake up")
                break

            elif 'crazy GK tricks' in query:
                kit.playonyt("Crazy GkTrick")

            elif 'exam Guruji' in query:
                kit.playonyt("exam gurooji")

            elif 'Drishti IAS' in query:
                kit.playonyt("Drishti IAS")
            
        

            

            
                            
                


            
                
                

                    

            
            

            elif 'turn on light' in query:
                speak('Rahul is working on it')

            elif 'search on my server' in query or 'server' in query:
                    query = myCommand()
                    res  = client.query(query)
                    output = next(res.results).query
                    speak(output)

            
            

            
           
                        

                
                
                    
                    

                

            
            
            elif 'yadunath' in query:
                speak('okay')
                webbrowser.open('https://www.youtube.com/watch?v=P_8Dj3RtfPI')
            elif 'open tomb runner' in query:
                speak('okay')
                webbrowser.open('https://m.plonga.com/adventure/Temple-Run-2-Online-Tablet')        
            elif "what\'s up" in query or 'how are you' in query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
                speak(random.choice(stMsgs))

            elif "do you feel like poo" in query: 
                stMsgs = ['yes i am']
                speak(random.choice(stMsgs))        
            elif "what is my name" in query: 
                stMsgs = ['your name is rahul shah']
                speak(random.choice(stMsgs))

            elif 'you can sleep now' in query:
                speak('ok sir you can call me anytime sir')
                break
    

            elif 'sent email to' in query:
                speak('Who is the recipient? ')
                recipient = myCommand()

                if 'me' in recipient:
                    try:
                        speak('What should I say? ')
                        content = myCommand()
            
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.ehlo()
                        server.starttls()
                        server.login("Your_Username", 'Your_Password')
                        server.sendmail('Your_Username', "Recipient_Username", content)
                        server.close()
                        speak('Email sent!')

                    except:
                        speak('Sorry Sir! I am unable to send your message at this moment!')


            elif 'nothing' in query or 'abort' in query or 'stop' in query:
                speak('okay')
                speak('Bye Sir, have a good day.')
                sys.exit()
                
            
            elif 'hello' in query:
                speak('Hello Sir')

            
            elif 'bye' in query:
                speak('Bye Sir, have a good day.')
                sys.exit()
                                        
            
            


            

            else:
                query = query
                speak('Searching...')
                try:
                    try:
                        res = client.query(query)
                        results = next(res.results).query
                        speak('As per your Server - ')
                        speak('Got it.')
                        speak(results)
                        
                    except:
                        results = wikipedia.summary(query, sentences=2)
                        speak('Got it.')
                        speak('WIKIPEDIA says - ')
                        speak(results)
            
                except:
                    speak('i can not find the information sir')
            
            speak('Next Command! Sir!')

