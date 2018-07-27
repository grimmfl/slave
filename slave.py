import speech_recognition as sr
import os
import spotify
from gtts import gTTS
from weather_class import weather
import subprocess


class Slave:
    def __init__(self):
        self.dict = {
            "MUSIK": {"SPIELE": self.music,
                      "SPIEL": self.music,
                      "STOPP": spotify.pause,
                      "STOPPE": spotify.pause,
                      "LIED": {"NÄCHSTES": spotify.skip,
                               "ÜBERSPRINGE": spotify.skip,
                               "ZURÜCK": spotify.prev,
                               "VORHERIGES": spotify.prev,
                               "DAVOR": spotify.prev}},
            "WETTER": self.weather
        }
        self.listener = sr.Recognizer()
        self.is_awake = False

    def menu(self):
        input = self.listen().upper()
        print(input)

        if "MARTIN" in input:
            self.speak("Hallo")
            self.is_awake = True
        if self.is_awake:
            for word in input.split(" "):
                if word in self.dict.keys():
                    if type(self.dict[word]) == type(self.listen):
                        self.dict[word](input)
                    else:
                        for word2 in input.split(" "):
                            if word2 in self.dict[word].keys():
                                if type(self.dict[word][word2]) == type(self.listen):
                                    self.dict[word][word2](input)
                                else:
                                    for word3 in input.split(" "):
                                        if word3 in self.dict[word][word2].keys():
                                            if type(self.dict[word][word2][word3]) == type(self.listen):
                                                self.dict[word][word2][word3](input)

    def weather(self, input):
        location = ""
        if "IN" in input:
            input_list = input.split(" ")
            for i in range(0, len(input_list)):
                if input_list[i] == "IN":
                    location = input_list[i + 1]
        self.speak(weather(loc=location))

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
            subprocess.call(["ping", "www.google.de", "-c 1"])
        except:
            self.speak("Keine Verbindung möglich, bitte stelle eine Internetverbindung her!")
            return False
        return True

    def music(self, input):
        if bytes("spotify", "utf-8") not in subprocess.check_output(["ps", "-e"]):
            subprocess.call(["spotify"])
        isConnected = self.is_connected()
        if isConnected:
            self.speak("Welche Musik willst du hören?")
            music = self.listen()
            spotify.play(music)
        else:
            return


    def speak(self, text):
        tts = gTTS(text=text, lang="de")
        tts.save("temp.mp3")
        subprocess.call(["mpg123", "temp.mp3"])
        os.remove("temp.mp3")




s = Slave()
while True:
    s.menu()

