import subprocess
import sys
import webbrowser
import pyttsx3
import os
import psutil
import pywhatkit
import pyautogui
import datetime
import wikipedia
import pyjokes
import requests

# --------------------------
# Auto Dependency Installer
# --------------------------
required_packages = ["speechrecognition", "pyttsx3", "pyaudio", "psutil", 
                     "pywhatkit", "pyautogui", "wikipedia", "pyjokes", "requests"]

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# --------------------------
# Voice Setup
# --------------------------
engine = pyttsx3.init()
try:
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    USE_VOICE = True
except:
    print("PyAudio or SpeechRecognition not available. Falling back to typing commands.")
    USE_VOICE = False

# --------------------------
# Speak function
# --------------------------
def speak(text):
    engine.say(text)
    engine.runAndWait()
    print("Jarvis:", text)

# --------------------------
# Listen function with fallback
# --------------------------
def listen():
    if USE_VOICE:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening...")
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                print("You said:", command)
                return command.lower()
        except:
            speak("Voice command failed, please type your command.")
            return input("You: ").lower()
    else:
        return input("You: ").lower()

# --------------------------
# Command Helper
# --------------------------
def process_multiple_commands(command):
    separators = [" and ", " then ", ","]
    for sep in separators:
        if sep in command:
            return [c.strip() for c in command.split(sep) if c.strip()]
    return [command]

# --------------------------
# App Functions
# --------------------------
def open_app(command):
    speak("Opening apps skipped in REPL/typing mode.")  # Optional: Can implement PC apps

def close_app(command):
    speak("Closing apps skipped in REPL/typing mode.")  # Optional: Can implement PC apps

# --------------------------
# System Functions
# --------------------------
def lock_pc(command): speak("Lock PC skipped")
def shutdown_pc(command): speak("Shutdown skipped")
def restart_pc(command): speak("Restart skipped")
def sleep_pc(command): speak("Sleep skipped")

# --------------------------
# Music Controls
# --------------------------
def play_music(command):
    song_name = command.replace("play", "").replace("music", "").strip()
    if song_name:
        speak(f"Playing {song_name} on YouTube")
        pywhatkit.playonyt(song_name)
    else:
        speak("Playing random music on YouTube")
        pywhatkit.playonyt("music")

def pause_music(): speak("Pause music skipped in REPL/typing")
def resume_music(): speak("Resume music skipped in REPL/typing")

# --------------------------
# Scolding
# --------------------------
def scolding(command):
    bad_words = {
        "fuck": "Aye! Don’t abuse me bro, I’m your assistant not your enemy.",
        "motherfucker": "Talk with respect bro!",
        "bitch": "Careful bro, don’t make me angry.",
        "idiot": "Haha, if I am idiot then who made me? You did bro!",
        "stupid": "No bro, I’m still smarter than most humans."
    }
    for word, reply in bad_words.items():
        if word in command:
            speak(reply)
            return True
    return False

# --------------------------
# Extra Features
# --------------------------
def list_operations():
    speak("""
I can perform:
1. Play music
2. Tell time/date
3. Google search
4. Wikipedia info
5. Weather info
6. Jokes
7. Respond to bad words
8. Exit
""")

def open_website(command):
    site = command.replace("open website", "").strip()
    if site:
        url = f"https://{site}.com"
        webbrowser.open(url)
        speak(f"Opening {site} website")

def tell_time_date(command):
    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}")
    elif "date" in command:
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {today}")

def google_search(command):
    query = command.replace("search", "").strip()
    if query:
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query} on Google")

def wikipedia_summary(command):
    topic = command.replace("tell me about", "").strip()
    try:
        summary = wikipedia.summary(topic, sentences=2)
        speak(summary)
    except:
        speak("Couldn't fetch info from Wikipedia.")

def weather_report(command):
    city = command.replace("weather in", "").strip()
    if city:
        api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            response = requests.get(url).json()
            temp = response['main']['temp']
            desc = response['weather'][0]['description']
            speak(f"{city}: {temp}°C, {desc}")
        except:
            speak("Couldn't fetch weather info.")

def tell_joke(command):
    joke = pyjokes.get_joke()
    speak(joke)

# --------------------------
# Command Handler
# --------------------------
def handle_command(command):
    if scolding(command): return
    if "operation" in command or "operations" in command: list_operations(); return
    if "open website" in command: open_website(command)
    elif "play" in command: play_music(command)
    elif "pause" in command: pause_music()
    elif "resume" in command: resume_music()
    elif "hello" in command: speak("Hello bro! How are you today?")
    elif "time" in command or "date" in command: tell_time_date(command)
    elif "search" in command: google_search(command)
    elif "tell me about" in command: wikipedia_summary(command)
    elif "weather in" in command: weather_report(command)
    elif "joke" in command: tell_joke(command)
    elif "exit" in command or "quit" in command:
        speak("Goodbye bro!"); raise StopIteration
    else: speak("I can't do that.")

# --------------------------
# Main Loop
# --------------------------
speak("Jarvis is online! Say 'Jarvis' to wake me up (or type commands).")

while True:
    try:
        command = listen()
        if "jarvis" in command:  # Wake word
            speak("Yes bro, I am listening!")
            while True:
                try:
                    inner_command = listen()
                    commands = process_multiple_commands(inner_command)
                    for cmd in commands:
                        handle_command(cmd)
                except StopIteration:
                    break
    except StopIteration:
        break
