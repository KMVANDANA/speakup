import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("good morning")
    elif 12 <= hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am David. How can I help you?")
   

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=20)  # Increased timeout to 5 seconds
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f'user said: {query}')
        except Exception as e:
            print(e)
            print("Say that again, please.")
            return "None"
        return query.lower()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=5)
            speak('according to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
        elif 'open spotify' in query:
            webbrowser.open("https://www.spotify.com")
        elif 'david time please' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")
        elif 'thank you' in query:
            speak("You're most welcome")
        elif 'open code' in query:
            path = "B:\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'open mca notes' in query:
            path = "B:\\mca"
            os.startfile(path)
        elif 'open wallpaper' in query:
            path = "B:\\wallpaper"
            os.startfile(path)
        elif 'bye bye' in query:
            speak("okay bye take care")
            break
