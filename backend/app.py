from flask import Flask, session, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler
from googleapiclient.discovery import build
    
load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)

CORS(app, resources={r"/*": {"origins": "*"}}) 

scope = [
     "user-read-email",
     "playlist-read-private",
     "playlist-modify-private",
     "playlist-modify-public",
     "playlist-read-collaborative"
    ]

cache_handler = FlaskSessionCacheHandler(session)

sp_oauth = SpotifyOAuth(
    client_id = os.getenv('CLIENT_ID'),
    client_secret = os.getenv('CLIENT_SECRET'),
    redirect_uri = os.getenv('REDIRECT_URI'),
    scope = scope,
    cache_handler = cache_handler,
    show_dialog = True
)

sp = Spotify(auth_manager=sp_oauth)

if __name__ == '__main__':
    app.run(debug=True)