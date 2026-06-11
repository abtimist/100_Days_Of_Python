from ytmusicapi import YTMusic
from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

URL = "https://appbrewery.github.io/bakeboard-hot-100/"
response = requests.get(f"{URL}/{date}")
web_page = response.text
soup = BeautifulSoup(web_page,'html.parser')

title_tag = soup.find_all(name='h3', class_='chart-entry__title')

music_titles = [title.getText() for title in title_tag]

# print(music_titles)

playlist_title=f"{date} Billboard 100"

yt = YTMusic("browser.json")

available_playlists=yt.get_library_playlists()
titles=[]

for i in range(len(available_playlists)):
    titles.append(available_playlists[i]['title'])

if playlist_title not in titles:
    playlist_id = yt.create_playlist(title=playlist_title, description= "Go back in time with music")
else:
    for playlist in available_playlists:
        if playlist['title'] == playlist_title:
            playlist_id = playlist['playlistId']
            break
music_ids=[]

for song in music_titles:
    try:
        musicId=yt.search(query=song,filter='songs')[0]['videoId']
        music_ids.append(musicId)
    except Exception as e:
        print(f"Could not add '{song}': {e}")


yt.add_playlist_items(playlistId=playlist_id,videoIds=music_ids)


