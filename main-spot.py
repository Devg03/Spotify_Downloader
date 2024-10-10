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

# # Requesting the Spotify track ID from the user
print()
print("Please enter your Spotify track id: ", end = ' ')
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

# Function to call YT API to get the track vid url's details
def get_yt_video_url(api_key, artists_name, track_name):
    yt = build('youtube', 'v3', developerKey=os.getenv("YT_API_KEY"))

    search_response = yt.search().list(
        q = f'{artist_name} {track_name}',
        part = 'snippet',
        maxResults = 1,
        type = "video"
    ).execute()

    if search_response['items']:
        yt_vid_id = search_response['items'][0]['id']['videoId'] # Video ID
        return yt_vid_id
    else:
        return "No video found."

# Stores the youtube video id to generate query string
yt_vid_id = get_yt_video_url(os.getenv('YT_API_KEY'), artists_name = artist_name, track_name = track_name)
# YT-MP3 RAPID API CALLS 
# -> 50 REQUESTS A MONTH & 1000 REQUEST PER HOUR (FREE PLAN)

# URL Endpoint for the RapidAPI
url = "https://youtube-mp3-downloader2.p.rapidapi.com/ytmp3/ytmp3/"

# Query String for RapidApi
querystring = {"url":f"https://www.youtube.com/watch?v={yt_vid_id}","quality":"320"}

headers = {
    "x-rapidapi-key": os.getenv('RAPID_API_KEY'),
    "x-rapidapi-host": "youtube-mp3-downloader2.p.rapidapi.com"
}

# GET request to YT-MP3 RapidAPI
response = requests.get(url, headers=headers, params=querystring)

# Filters out the download link and prints it for testing
print(response.json()['dlink'])