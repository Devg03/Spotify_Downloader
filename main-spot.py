import os
import spotipy
import json
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

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

# # Requesting the track ID from the user
print("Please enter your track id: ", end = ' ')
track_id = input()

# # Calling Spotify API to receive the track name from its ID
track_info = sp.track(track_id=track_id, market=None)
print(track_info['name'])

# Calling Spotify API to receive the top tracks of an artist and possibly extract the track IDs
print("Enter the artist's id: ", end = ' ')
artist_id = input()

# Enumerating the top 10 tracks of the artists
artists_top_tracks = sp.artist_top_tracks(artist_id = artist_id, country='US')
for idx, item in enumerate(artists_top_tracks['tracks']):
    print(idx + 1,item['name']) 