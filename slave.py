import speech_recognition as sr
import os
import music_crawler
from gtts import gTTS
from weather_class import weather


class Slave:
    def __init__(self):
        self.listener = sr.Recognizer()
        self.is_awake = False

    def menu(self):
        input = self.listen().upper()
        print(input)

        if "MARTIN" in input:
            self.speak("Hallo")
            self.is_awake = True
        if self.is_awake:
            if "SPIEL" in input and "MUSIK" in input:
                self.music()
            elif "STOPPE MUSIK" in input:
                self.stop_music()
            elif "WETTER" in input:
                self.speak(weather())
            elif "GEH" in input and "SCHLAFEN" in input:
                self.speak("Gute Nacht")
                self.is_awake = False

    def listen(self):
        with sr.Microphone() as source:
            print("Höre zu...")
            self.listener.adjust_for_ambient_noise(source)
            audio = self.listener.listen(source)
        try:
            text = self.listener.recognize_google(audio, language="de_DE")
        except sr.UnknownValueError:
            if self.is_awake:
                self.speak("Das habe ich leider nicht verstanden.")
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
            address = music_crawler.get_address(music)
            os.system('start firefox.exe "https://www.youtube.com/' + address + '"')
        else:
            return

    def stop_music(self):
        os.system("taskkill /IM firefox.exe")

    def speak(self, text):
        tts = gTTS(text=text, lang="de")
        tts.save("temp.mp3")
        os.system("mpg123 temp.mp3")
        os.remove("temp.mp3")




s = Slave()
while True:
    s.menu()

