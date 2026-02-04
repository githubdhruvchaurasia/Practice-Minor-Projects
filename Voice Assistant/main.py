import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize the user's voice
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Sorry, I didn't catch that. Could you please repeat?")
            return None
        return query

# Main function for the assistant
def voice_assistant():
    speak("Hello! I am your voice assistant. How can I help you today?")
    
    while True:
        query = take_command()

        if query is None:
            continue

        # Handling basic commands
        query = query.lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(f"According to Wikipedia, {results}")
        
        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")

        elif 'time' in query:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            print(current_time)
            speak(f"The time is {current_time}")

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye! Have a great day!")
            break

        else:
            speak("I am sorry, I can't help with that right now.")

# Start the voice assistant
voice_assistant()
