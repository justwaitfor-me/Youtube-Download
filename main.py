import pytube
import os
from datetime import date
import requests
from bs4 import BeautifulSoup
import tkinter
from tkinter import filedialog
import time

def get_channelid(q): 
    """
    The function `get_channelid` takes a search query as input and returns the channel name and channel
    ID of the first YouTube channel that matches the query.
    
    :param q: The parameter "q" is the search query. It is the term or phrase that you want to search
    for on YouTube. It can be any string value
    """
   
    url = "https://youtube.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": q,
        "type": "channel",
        "key": "AIzaSyCb0oSyMUeqkPqCXI240uZZFT8eMh11i5Q",
    }

    # Senden der Anfrage und Speichern der Antwort
    response = requests.get(url, params=params)

    # Prüfen des Statuscodes
    if response.status_code == 200:
        data = response.json()["items"][0]

    else:
        return(f"Error: {response.status_code}")
        
    return([data['snippet']['channelTitle'], data['id']['channelId']])

def get_videourl():
    """
    The function `get_videourl()` retrieves the video URLs from a YouTube channel's XML feed.
    :return: The function `get_videourl()` returns a list of video URLs.
    """
    
    #get channel id
    q = input("Enter Youtuber Name:\n>")
    channel_id = get_channelid(q)

    print(f"Name: {channel_id[0]}\nId: {channel_id[1]}\n")

    # URL der XML-Datei
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id[1]}"

    # XML-Datei abrufen
    response = requests.get(url)

    # BeautifulSoup-Parser erstellen
    soup = BeautifulSoup(response.content, "xml")

    # Alle <entry>-Elemente finden
    entries = soup.find_all("entry")

    # Liste für HREFs erstellen
    hrefs = []

    # Alle <link>-Elemente in <entry>-Elementen durchlaufen
    for entry in entries:
        links = entry.find_all("link")
        for link in links:
            hrefs.append(link["href"])

    # Liste der HREFs ausgeben
    return(hrefs)


def download(url, pfad):
    """
    The function `download` takes a URL and a file path as input, creates a Pytube object, retrieves the
    highest resolution video from the URL, and downloads it to the specified file path.
    
    :param url: The `url` parameter is the URL of the YouTube video that you want to download. It should
    be a string
    :param pfad: The parameter "pfad" represents the path where you want to save the downloaded video.
    It should be a string that specifies the directory where you want to save the video file. For
    example, if you want to save the video in the current working directory, you can pass "." as the
    value for
    """
    # Pytube-Objekt erstellen
    youtube = pytube.YouTube(url)
    
    # Höchste Auflösung des Videos abrufen
    video = youtube.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

    # Video herunterladen
    video.download(pfad)


# The code is a Python script that allows you to download videos from a YouTube channel.
print("Youtube Video Downloader")

# get video hrefs
url_list = get_videourl()

print(f"Urls found: {len(url_list)}")
repeat = input("how many should be downloaded?\n>")

# prevents an empty tkinter window from appearing
tkinter.Tk().withdraw()
folder_path = filedialog.askdirectory()

# Pfad zum Speicherort des Downloads angeben
today = date.today()
pfad = f"{folder_path}/{today}"
print(f"Videos are saved in '{pfad}'!")

# Ordner erstellen
os.mkdir(pfad)

print("\nstarting download...")
time.sleep(5)
for i in range(1, int(repeat)+1):
    download(url_list[i], pfad)
    print(f"{i}/{int(repeat)}")
    
# Ausgabe
print("downloaded successfully!")
