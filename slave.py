import speech_recognition as sr
import os
import crawler
from gtts import gTTS
import pyglet
import time

class Slave:
    def __init__(self):
        self.listener = sr.Recognizer()

    def menu(self):
        self.test()
        input = self.listen().upper()

        if "SPIELE MUSIK" in input:
            self.music()
        elif "STOPPE MUSIK" in input:
            self.stop_music()

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
            print("No connection, try again!")
            return False
        return True

    def music(self):
        isConnected = self.is_connected()
        if isConnected:
            print("Welche Musik?")
            music = self.listen()
            address = crawler.get_address(music)
            os.system('start firefox.exe "https://www.youtube.com/' + address + '"')
        else:
            return

    def stop_music(self):
        os.system("taskkill /IM firefox.exe")

    def test(self):
        tts = gTTS(text="Hallo Felix wie geht es dir?", lang="de")
        tts.save("hello.mp3")
        voice = pyglet.media.load("hello.mp3", streaming=False)
        voice.play()
        time.sleep(voice.duration)
        os.remove("hello.mp3")



s = Slave()
while True:
    s.menu()

