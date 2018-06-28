from pygame import *
from bs4 import BeautifulSoup
from selenium import webdriver


class Weather:
    def __init__(self):
        self.temperature = ""

    def play(self):
        self.crawl()
        mixer.music.load("audio/words/aktuelleTemperatur.wav")
        mixer.music.play()

        while mixer.music.get_busy():
            time.Clock().tick(10)

        mixer.music.load("audio/words/" + self.temperature + ".wav")
        mixer.music.play()

        while mixer.music.get_busy():
            time.Clock().tick(10)

        mixer.music.load("audio/words/grad.wav")
        mixer.music.play()

        while mixer.music.get_busy():
            time.Clock().tick(10)

    def crawl(self):
        query = "https://www.google.com/search?q=wetter"
        browser = webdriver.Chrome()
        browser.get(query)
        plain_text = browser.page_source
        browser.quit()
        soup = BeautifulSoup(plain_text, "html.parser")

        for text in soup.findAll('span', {'id': 'wob_tm'}):
            self.temperature = text.text
            break


mixer.init()
w = Weather()
w.play()
