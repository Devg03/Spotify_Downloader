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
    return redirect(url_for('get_yt_id'))

@app.route('/callback')
def callback():
    sp_oauth.get_access_token(request.args['code'])
    return redirect(url_for('get_yt_id'))

def get_track_data():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    
    track_id = "https://open.spotify.com/track/1UsQe17Ef7tV1ahFqHEFR3?si=30456dc2e9084347"
    track_data = sp.track(track_id = track_id)

    return track_data

def get_track():
    track_data = get_track_data()
    track_name = track_data['name']
    return track_name
    
def get_artist():
    track_data = get_track_data()
    artist_id = track_data["artists"][0]["id"]
    artist_data = sp.artist(artist_id = artist_id)
    artist_name = artist_data['name']

    return artist_name

@app.route('/display')
def display():
    track_name = get_track()
    artist_name = get_artist()

    return track_name + " by: " + artist_name

@app.route('/get_yt_id')
def get_yt_id():
    track_name = get_track()
    artist_name = get_artist()
    yt = build('youtube', 'v3', developerKey=os.getenv("YT_API_KEY"))
    
    search_response = yt.search().list(
        q = f'{track_name} {artist_name}',
        part = 'snippet',
        maxResults = 1,
        type = "video"
    ).execute()

    if search_response['items']:
        yt_vid_id = search_response["items"][0]["id"]["videoId"]
        return yt_vid_id
    else:
        return "No Video Found."

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
