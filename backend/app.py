from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from googleapiclient.discovery import build
    
load_dotenv()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 

if __name__ == '__main__':
    app.run(debug=True)