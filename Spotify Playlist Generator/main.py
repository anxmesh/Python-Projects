############################ Imports ############################
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

############################ Scraping Billboard's top 100 ############################

DATE = input("What date would you like to travel back to (musically ofcourse - I ain't no Hawking 😅)? Please enter "
             "in the YYYY-MM-DD format: ")
URL = f"https://www.billboard.com/charts/hot-100/{DATE}"
print(f"Chosen date is: {DATE}")

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, 'html.parser')
titles_raw = soup.find_all("span", class_="chart-element__information__song text--truncate color--primary")
artists_raw = soup.find_all("span", class_="chart-element__information__artist text--truncate color--secondary")

titles = [title.getText() for title in titles_raw]
artists = [artist.getText() for artist in artists_raw]
print(titles)
print(artists)

song_details = []
for i in range(100):
    song_details.append(f"{titles[i]} - {artists[i]}")

print(song_details)

############################ Spotify API setup ############################

# Change the following things to your personal details from spotify dashboard
client_id = "YOUR PERSONAL CLIENT ID"
client_secret = "YOUR PERSONAL CLIENT SECRET"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

############################ Searching for songs on Spotify ############################
song_uris = []
year = DATE.split("-")[0]
for song in titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

############################ Creating the Playlist ############################
playlist = sp.user_playlist_create(user=user_id, name=f"{DATE} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
