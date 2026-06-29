"""
Jarvis AI Pro
Voice Engine
Author : Vishal Pawar
"""

import json
import queue
import sounddevice as sd
import pyttsx3

from vosk import Model, KaldiRecognizer
from config import *

print("[VOICE] Loading Voice Engine...")

# -------------------------------
# Text To Speech
# -------------------------------

engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")

if len(voices) > 0:
    engine.setProperty("voice", voices[0].id)


def speak(text):
    print(f"Jarvis : {text}")
    engine.say(text)
    engine.runAndWait()


# -------------------------------
# Vosk Speech Recognition
# -------------------------------

MODEL_PATH = "models/vosk-model-small-en-us-0.15"

print("[VOICE] Loading Vosk Model...")

model = Model(MODEL_PATH)

recognizer = KaldiRecognizer(model, 16000)

audio_queue = queue.Queue()


def callback(indata, frames, time, status):
    if status:
        print(status)
    audio_queue.put(bytes(indata))

# -------------------------------
# Listen Function
# -------------------------------

def listen():
    print("\nListening...")

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=callback,
    ):

        while True:

            data = audio_queue.get()

            if recognizer.AcceptWaveform(data):

                result = json.loads(recognizer.Result())

                text = result.get("text", "").lower()

                if text:
                    print("You :", text)
                    return text


# -------------------------------
# Test
# -------------------------------

if __name__ == "__main__":

    speak("Voice engine loaded successfully.")

    while True:

        command = listen()

        if command == "exit":
            speak("Goodbye Vishal")
            break