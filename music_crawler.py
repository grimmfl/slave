from selenium import webdriver
from bs4 import BeautifulSoup

youtube = "https://www.youtube.com/results?search_query="

def get_address(keyword):
    query = youtube + keyword + "+playlist"
    browser = webdriver.Chrome()
    browser.get(query)
    plain_text = browser.page_source
    browser.quit()
    soup = BeautifulSoup(plain_text, "html.parser")

    for link in soup.findAll('a', {'class': 'yt-simple-endpoint style-scope ytd-playlist-renderer'}):
       href = link.get('href')
       return href