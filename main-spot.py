import os
import spotipy
import requests
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from googleapiclient.discovery import build

load_dotenv()

scope = [
     "user-read-email",
     "playlist-read-private",
     "playlist-modify-private",
     "playlist-modify-public",
     "playlist-read-collaborative"
 ]

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = os.getenv('CLIENT_ID'),
                                                 client_secret = os.getenv('CLIENT_SECRET'), 
                                                 redirect_uri= os.getenv('REDIRECT_URI'),
                                                 scope=scope))

yt_api_endpoint = "https://youtube-mp3-downloader2.p.rapidapi.com/ytmp3/ytmp3/"

# # Requesting the track ID from the user
print()
print("Please enter your track id: ", end = ' ')
track_id = input()

# # Calling Spotify API to receive the track name from its ID
track_info = sp.track(track_id=track_id, market=None)
# Filtering the artists' name from the track dict response
track_name = track_info['name']
# Filtering the artists' id from the track dict response
artist_id = track_info["artists"][0]["id"]
# Fetching artists' data from the artists' id
artist_data = sp.artist(artist_id = artist_id)
# Filtering the artists' name from the dict given by spotify API as the response
artist_name = artist_data['name']

print()
print(f'Track name: {track_name}, Artist: {artist_name}')

def get_yt_video_url(api_key, artists_name, track_name):
    yt = build('youtube', 'v3', developerKey=os.getenv("YT_API_KEY"))

    search_response = yt.search().list(
        q = f'{artist_name} {track_name}',
        part = 'snippet',
        maxResults = 1,
        type = "video"
    ).execute()

    if search_response['items']:
        video_id = search_response['items'][0]['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        print(video_url)
    else:
        return "No video found."

get_yt_video_url(os.getenv('YT_API_KEY'), artists_name = artist_name, track_name = track_name)

# headers = {
# 	"x-rapidapi-key": "Sign Up for Key",
# 	"x-rapidapi-host": "youtube-mp3-downloader2.p.rapidapi.com"
# }

# response = requests.get(yt_api_endpoint, headers=headers, params=querystring)

# print(response.json())