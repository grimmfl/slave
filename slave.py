import speech_recognition as sr
import os
import crawler
import time

class Slave:
    def __init__(self):
        self.listener = sr.Recognizer()

    def menu(self):
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
            os.system("start audio\\no_connection.wav")
            return False
        return True

    def music(self):
        isConnected = self.is_connected()
        if isConnected:
            os.system("start audio\\which_music.wav")
            time.sleep(4)
            music = self.listen()
            address = crawler.get_address(music)
            os.system('start firefox.exe "https://www.youtube.com/' + address + '"')
        else:
            return

    def stop_music(self):
        os.system("taskkill /IM firefox.exe")


s = Slave()
while True:
    s.menu()

