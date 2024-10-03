import os
import json
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from requests_oauthlib import OAuth2Session

# Leveraging dotenv to keep the spotify credentials confidential
load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URL')

# OAuth endpoints given in the Spotify API documentation
authorization_base_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"

# https://developer.spotify.com/documentation/general/guides/authorization/scopes/
scope = [
     "user-read-email",
     "playlist-read-private",
     "playlist-modify-private",
     "playlist-modify-public",
     "playlist-read-collaborative"
 ]

spotify = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

# Redirect user to Spotify for authorization
authorization_url, state = spotify.authorization_url(authorization_base_url)
print('Please go here and authorize: ', authorization_url)

# Get the authorization verifier code from the callback url
redirect_response = input('\n\nPaste the full redirect URL here: ')

auth = HTTPBasicAuth(client_id, client_secret)

# Fetch the access token
token = spotify.fetch_token(token_url, auth=auth,
         authorization_response=redirect_response)

print(token)

# Fetch a protected resource
r = spotify.get('https://api.spotify.com/v1/me')
print(r.content)

print("Please enter the track id: ", end='')
track_id = input('')
track_response = requests.get('https://api.spotify.com/v1/tracks/' + track_id)

if track_response.status_code == 200:
    track_detail = track_response.json()
