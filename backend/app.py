from flask import Flask, session, request, redirect, url_for
from flask_cors import CORS
import os
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler
from googleapiclient.discovery import build
    
load_dotenv()
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.urandom(64)
cache_handler = FlaskSessionCacheHandler(session)

scope = "user-read-email","playlist-read-private","playlist-modify-private","playlist-modify-public","playlist-read-collaborative"

sp_oauth = SpotifyOAuth(
    client_id = os.getenv('CLIENT_ID'),
    client_secret = os.getenv('CLIENT_SECRET'),
    redirect_uri = os.getenv('REDIRECT_URI'),
    scope = scope,
    cache_handler = cache_handler,
    show_dialog = True
)

sp = Spotify(auth_manager=sp_oauth)

@app.route('/')
def home():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    return redirect(url_for('get_tracks'))

@app.route('/callback')
def callback():
    sp_oauth.get_access_token(request.args['code'])
    return redirect(url_for('get_tracks'))

@app.route('/get_tracks')
def get_tracks():

    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    
    track_id = "https://open.spotify.com/track/1UsQe17Ef7tV1ahFqHEFR3?si=30456dc2e9084347"

    track_info = sp.track(track_id = track_id)
    track_name = '<br>'.join({track_info['name']})

    return track_name

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
