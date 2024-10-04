import os
import spotipy
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

# Requesting the track ID
print("Please enter your track id: ", end = ' ')
track_id = input()

# Calling Spotify API to receive the track name from its ID
track_info = sp.track(track_id=track_id, market=None)
print(track_info['name'])
