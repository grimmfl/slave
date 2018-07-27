import os
import spotipy
from spotipy import oauth2

ccm = oauth2.SpotifyClientCredentials(client_id="ad2bce95e1e34fa3830b79f1b69b6fa4",
                                      client_secret="457ba3cbc0bb4f508e668626bda70592")

token = ccm.get_access_token()
sp = spotipy.Spotify(token)


def play(music=""):
    if music == "":
        os.system("./sp play")
    elif music is not "":
        uri = get_uri(music)
        os.system("./sp open " + uri)


def pause(*input):
    os.system("./sp pause")


def skip(*input):
    os.system("./sp next")


def prev(*input):
    os.system("./sp prev")


def get_uri(music):
    results = sp.search(q=music, limit=1)
    return results["tracks"]["items"][0]["uri"]
