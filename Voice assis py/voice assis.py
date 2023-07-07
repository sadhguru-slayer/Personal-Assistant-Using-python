import speech_recognition as sr
import pyttsx3
import datetime
from datetime import date
from datetime import time
import wikipedia
import webbrowser
import os
from time import sleep
import pyjokes
import subprocess
from pywinauto.application import Application
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)

    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if (hour >= 0 and hour < 12):
        speak(f"Good Monring!")


    elif hour >= 12 and hour < 18:
        speak(f"Good After Noon!")

    else:
        speak(f"Good Evening!")



def takecommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print('Recognizing....')
        query=r.recognize_google(audio,language='en-in')
        print(f":User Said: {query}\n")

    except:
        print('Say That Again Please....')
        return "None"
    return query

def main():

    while True:
        try:
            query = takecommand().lower()

            if 'hello' in query:
                speak("Hello sir this is HCF created by CMR tians...how may i help you?")
                
            if 'wish me' in query:
                wishme()
            if 'wikipedia' in query:
                speak("seraching .......")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak("Accroding to wikipedia")
                speak(result)
            elif 'open youtube' in query:
                speak("about what you want to search on youtube")
                s = takecommand()                           
                webbrowser.open("www.youtube.com/results?search_query=" + s + "")
                speak(f"opening youtube!")
            elif 'open google' in query:
                webbrowser.open("google.com")
                speak(f"opening google !")
        
            elif 'the time' in query:
                strtime = datetime.datetime.now().strftime("%I ""%M")

                speak(f" the time is{strtime}")
            elif 'open facebook' in query:
                webbrowser.open("facebook.com")
                speak(f"opening Facebook!")

            elif 'open instagram' in query:
                webbrowser.open("instagram.com")
                speak('opening Instagram')

            elif 'open netflix' in query:
                webbrowser.open("netflix.com")
                speak('opening Netflix....mind if i watch with you')

            elif 'search' in query:
                s = webbrowser.open(query)
                speak('sure')
                

            elif 'who is' in query:
                webbrowser.open(query)

            elif 'how are you' in query:
                speak(f"hello I'm fine ! How are you")

            elif 'how old are you' in query:
                speak("I'm 1 month. and 12 days old")


            elif 'good' in query or 'well' in query:
                speak(f'great to hear that you are well')
            elif "will you be my gf" in query or "will you be my bf" in query:

                speak("I'm not sure about, may be you should give me some time")

            elif 'today' in query:
                speak("It is")
                speak(date.today())
                speak("today")
            elif "who made you" in query or "who created you" in query:
                speak("I have been created by CMR tians")

            elif 'joke' in query:
                s = pyjokes.get_joke(language='en', category='all')
                speak(s)
                

            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to Locate..opening maps")
                speak(location)
                webbrowser.open("https://www.google.com/maps/place/" + location + "")


            elif "weather" in query:
                speak(" City name ")
                print("City name : ")
                city_name = takecommand()
                webbrowser.open("https://www.accuweather.com/en/in/" + city_name + "/189231/weather-forecast/189231")
                speak("opening wether for")
                speak(city_name)

            elif 'help me' in query:
                speak(f"ofcourse  ! how can i help you ")
                speak(f'question !')
                s = takecommand()
                print(s)
                speak(
                    "There are 3 thing that i can do for you sir i can search for it on google or youtube or wikipedia")
                speak(f"where i should to serach ")
                s1 = takecommand().lower()
                if s1 == 'google':
                    speak(f"opening  google !")
                    webbrowser.open(
                        "www.bing.com/search?q=" + s + "")
                                       

                if s1 == 'YouTube' in query:
                    speak(f"opening youtube!")
                    webbrowser.open("www.youtube.com/results?search_query=" + s + "")
                    
                if s1 == 'wikipedia' in query:
                    speak("Accroding to wikipedia")
                    result = wikipedia.summary(s, sentences=2)

            elif "meet my friend" in query:
                speak("hello !what is your friends name ")
                s = takecommand().lower()
                speak(f"nice to meet you {s} ! have a good day!")

            elif 'open calculator' in query:
                speak("open the calculator")
                subprocess.Popen("C:\\Windows\\System32\\calc.exe")
            elif 'close' in query:
                speak("closing the window")
 

                pyautogui.hotkey('alt', 'f4')

            elif 'minimise the windows ' in query or 'minimise the window' in query:
                speak("minimizing the window")
                pyautogui.hotkey('Win', 'd')

            elif 'maximize the window' in query:
                speak("maximizeing windows")
                pyautogui.hotkey('Win', 'd')

            elif 'new tab' in query:
                pyautogui.hotkey('ctrl', 't')

            elif 'new file' in query:
                pyautogui.hotkey('ctrl', 'n')

            elif 'switch the windows' in query or 'switch the tab' in query:
                pyautogui.hotkey('ctrl', 'shift', 'tab')

            elif 'volume up' in query:
                speak('valume up sir')
                pyautogui.hotkey('volumeup')

            elif 'volume down' in query:
                speak('valume down sir')
                pyautogui.hotkey('volumedown')


            elif 'push' in query or 'play' in query:
                speak('ok')
                pyautogui.press('Space')

            elif 'open chrome' in query:
                speak("opening broswer sir")
                p = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
                os.startfile(p)
                sleep(6)
            elif 'i want to search' in query:
                speak("ok sir please say what you want to write or search sir")
                s = takecommand()
                pyautogui.write(s)
                sleep(3)
                pyautogui.press('enter')

            elif 'exit' in query:
                speak("Thanks for giving me your time")
                exit()
            elif 'shutdown' in query or 'sleep my' in query:
                speak("shuting down")
                os.system("shutdown /h")

            elif "restart" in query:
                os.system('shutdown /r')
        except Exception as s:
            print(s)
            speak(f" i dont understand sir please give me some other commend")

if __name__ == "__main__":
    # jarvis()
    main()