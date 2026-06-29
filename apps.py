"""
Jarvis AI Pro
apps.py
"""

import os
import subprocess
import webbrowser
import pyautogui


# -----------------------------
# OPEN APPLICATIONS
# -----------------------------

def open_app(command):

    command = command.lower()

    try:

        if "chrome" in command:
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            return "Opening Chrome"

        elif "edge" in command:
            os.startfile(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
            return "Opening Edge"

        elif "notepad" in command:
            subprocess.Popen("notepad")
            return "Opening Notepad"

        elif "calculator" in command:
            subprocess.Popen("calc")
            return "Opening Calculator"

        elif "paint" in command:
            subprocess.Popen("mspaint")
            return "Opening Paint"

        elif "cmd" in command or "command prompt" in command:
            subprocess.Popen("cmd")
            return "Opening Command Prompt"

        elif "explorer" in command or "file manager" in command:
            subprocess.Popen("explorer")
            return "Opening File Explorer"

        elif "youtube" in command:
            webbrowser.open("https://youtube.com")
            return "Opening YouTube"

        elif "google" in command:
            webbrowser.open("https://google.com")
            return "Opening Google"

        elif "github" in command:
            webbrowser.open("https://github.com")
            return "Opening GitHub"

        return "Application not found"

    except Exception as e:
        return str(e)


# -----------------------------
# CLOSE APPLICATIONS
# -----------------------------

def close_app(command):

    command = command.lower()

    try:

        if "chrome" in command:
            os.system("taskkill /f /im chrome.exe")

        elif "edge" in command:
            os.system("taskkill /f /im msedge.exe")

        elif "notepad" in command:
            os.system("taskkill /f /im notepad.exe")

        elif "calculator" in command:
            os.system("taskkill /f /im CalculatorApp.exe")
            os.system("taskkill /f /im calculator.exe")

        elif "paint" in command:
            os.system("taskkill /f /im mspaint.exe")

        elif "cmd" in command:
            os.system("taskkill /f /im cmd.exe")

        return "Done"

    except Exception as e:
        return str(e)


# -----------------------------
# MEDIA CONTROLS
# -----------------------------

def media(command):

    command = command.lower()

    if "pause" in command:
        pyautogui.press("playpause")
        return "Music Paused"

    elif "resume" in command:
        pyautogui.press("playpause")
        return "Music Resumed"

    elif "play music" in command:
        webbrowser.open("https://music.youtube.com")
        return "Playing Music"

    elif "next" in command:
        pyautogui.press("nexttrack")
        return "Next Song"

    elif "previous" in command:
        pyautogui.press("prevtrack")
        return "Previous Song"

    elif "stop" in command:
        pyautogui.press("playpause")
        return "Stopped"

    elif "volume up" in command:
        pyautogui.press("volumeup")
        return "Volume Increased"

    elif "volume down" in command:
        pyautogui.press("volumedown")
        return "Volume Decreased"

    elif "mute" in command:
        pyautogui.press("volumemute")
        return "Muted"

    return "Done"