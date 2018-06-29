import speech_recognition as sr
import os
import crawler
from gtts import gTTS
import pyglet
import time
from weather_class import weather

class Slave:
    def __init__(self):
        self.listener = sr.Recognizer()
        self.is_awake = False

    def menu(self):
        input = self.listen().upper()
        print(input)

        if "MARTIN" in input:
            self.is_awake = True
        if "SPIELE MUSIK" in input or "SPIEL MUSIK" in input and self.is_awake:
            self.music()
        elif "STOPPE MUSIK" in input and self.is_awake:
            self.stop_music()
        elif "WETTER" in input and self.is_awake:
            self.speak(weather())

    def listen(self):
        with sr.Microphone() as source:
            print("Höre zu...")
            audio = self.listener.listen(source)
        try:
            text = self.listener.recognize_google(audio, language="de_DE")
        except:
            text = ""
        return text

    def is_connected(self):
        try:
            os.system("ping www.google.de -n 1")
        except:
            self.speak("Keine Verbindung möglich, bitte stelle eine Internetverbindung her!")
            return False
        return True

    def music(self):
        isConnected = self.is_connected()
        if isConnected:
            self.speak("Welche Musik willst du hören?")
            music = self.listen()
            print(music)
            address = crawler.get_address(music)
            os.system('start firefox.exe "https://www.youtube.com/' + address + '"')
        else:
            return

    def stop_music(self):
        os.system("taskkill /IM firefox.exe")

    def speak(self, text):
        tts = gTTS(text=text, lang="de")
        tts.save("temp.mp3")
        voice = pyglet.media.load("temp.mp3", streaming=False)
        voice.play()
        time.sleep(voice.duration)
        os.remove("temp.mp3")




s = Slave()
while True:
    s.menu()

