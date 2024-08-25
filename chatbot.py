import speech_recognition as sr
import pyttsx3
from datetime import datetime
import time  
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    with sr.Microphone() as source:
        print("Calibrating microphone for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5) 
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()  
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError as e:
            speak(f"Could not request results from the service; {e}")
            return None
        except sr.WaitTimeoutError:
            speak("Listening timed out. Please try again.")
            return None
def think_delay(seconds=1):
    time.sleep(seconds) 
def chatbot():
    speak("Hello, how can I help you today?")
    while True:
        query = listen()
        if query:
            think_delay(1) 
            print(f"Processing: {query}")  
            if "hello" in query:
                speak("Hi there! How can I assist you?")
            elif "your name" in query:
                speak("I am your AI voice assistant.")
            elif "how are you" in query:
                speak("I'm just a bunch of code, but I'm functioning as expected!")
            elif "time" in query:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                speak(f"The current time is {current_time}")
            elif "day" in query:
                now = datetime.now()
                current_day = now.strftime("%A")
                speak(f"Today is {current_day}")
            elif "date" in query:
                now = datetime.now()
                current_date = now.strftime("%Y-%m-%d")
                speak(f"Today's date is {current_date}")
            elif "weather" in query:
                speak("I'm unable to check the weather at the moment, but you can use your favorite weather app.")
            elif "exit" in query or "bye" in query:
                speak("Goodbye!")
                break
            else:
                speak("I'm not sure how to respond to that. Could you ask something else?")

if __name__ == "__main__":
    chatbot()
