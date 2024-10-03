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

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])