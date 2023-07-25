import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from googlesearch import search

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning!")
    elif hour > 12 and hour <= 14:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am JARVIS. How may I help you? ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

# Initializing Microsoft SpeechApi(sapi5)
engine = pyttsx3.init('sapi5')

# Getting Voices(Male/Female)
voices = engine.getProperty('voices')

# Setting voice to male voice
engine.setProperty('voice', voices[1].id)

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'google' in query:
            query2 = query.replace("google","")
            for j in search(query2, tld="co.in", num=1, stop=2):
                webbrowser.open(j)
        
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open reddit' in query:
            webbrowser.open("reddit.com")

        elif 'open spotify' in query or 'play music' in query:
            webbrowser.open("open.spotify.com")
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        
        elif 'take notes' in query:
            f = open('notes.txt','w')
            notes = takeCommand()
            f.write(notes)
            f.close()
        
        elif 'read notes' in query:
            f = open('notes.txt','r')
            print(f.read())
        
        elif 'exit' in query:
            break
