from flask import Flask, request, jsonify, send_from_directory
import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from googleapiclient.discovery import build
    
load_dotenv()
app = Flask(__name__, static_folder="../frontend/spoticry/build/", static_url_path="/")

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    input_value = data.get('input_data')
    


@app.route("/")
def start():
    return send_from_directory(app.static_folder, "index.html")
