import speech_recognition as sr
import pyttsx3

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User: {query}")
        return query.lower()
    except Exception as e:
        print(e)
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak("Hello, I am your custom voice assistant. How can I help you?")
while True:
    query = listen()
    if "hello" in query:
        speak("Hi, how can I help you?")
    elif "what can you do" in query:
        speak("I can respond to specific voice commands")
    elif "exit" in query:
        speak("Goodbye!")
        break
