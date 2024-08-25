import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I didn't understand that."

print("Hello! How can I help you today?")
speak("Hello! How can I help you today?")

while True:
    user_input = listen()

    if "hello" in user_input:
        speak("Hi! How are you?")
    elif "help" in user_input:
        speak("I can assist you with general information or answer questions.")
    elif "bye" in user_input:
        speak("Goodbye! Have a great day!")
        break
    else:
        speak("Sorry, I didn't understand that. Please try again!")