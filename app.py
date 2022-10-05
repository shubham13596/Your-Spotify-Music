import os
import sys
import uuid
import urllib
import requests
import statistics
from urllib.parse import urlencode
from collections import Counter


from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from flask import Flask


# Configure application
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    authentication_request_params = {
        'response_type': 'code',
        'client_id': os.getenv('CLIENT_ID'),
        'redirect_uri': os.getenv('REDIRECT_URI'),
        'scope': 'user-read-email user-read-private user-top-read',
        'state': str(uuid.uuid4()),
        'show_dialog': 'true'
        }

    auth_url = 'https://accounts.spotify.com/authorize/?' + urllib.parse.urlencode(authentication_request_params)

    return redirect(auth_url)

def get_access_token(authorization_code:str):
    spotify_request_access_token_url = 'https://accounts.spotify.com/api/token/?'
    body = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'client_id' : os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
        'redirect_uri': os.getenv('REDIRECT_URI')
    }

    response = requests.post(spotify_request_access_token_url, data = body)

    if response.status_code == 200:
        return response.json()
    raise Exception ('Failed to obtain Access token')

@app.route('/callback')
def callback():

    code = request.args.get('code')
    credentials = get_access_token(authorization_code=code)

    os.environ['token'] = credentials['access_token']

    #return f"Authentication successful. Access token: {credentials['access_token']}"

    return redirect('/your-music')


@app.route('/your-music')
def your_music():
    user_profile_url = 'https://api.spotify.com/v1/me?'
    user_top_items_url = 'https://api.spotify.com/v1/me/top/'
    audio_features_url = 'https://api.spotify.com/v1/audio-features/'

    limit_tracks = 18

    # NB: Add the access token to the request header
    headers = {
        'Authorization': f'Bearer {os.getenv("token")}'
    }

    request_params_artists = {
        'limit':18
    }

    request_params_tracks = {
        'limit': 18
    }

    #Retrieving User details via GET request to user profile endpoint
    user_profile = requests.get(user_profile_url, headers=headers)
    if user_profile.status_code == 200:
        user_profile = user_profile.json()
        display_name = user_profile['display_name']

    #Retrieving top Artists details via GET request to top artists endpoint
    top_artists_url = user_top_items_url + 'artists?' + urllib.parse.urlencode(request_params_artists)
    artists = requests.get(top_artists_url, headers = headers)
    if artists.status_code == 200:
        artists = artists.json()
        artists = artists['items']


        genres_list = []
        genres_text = []

        for i in artists:
            genres_list.append(i['genres'])

        for x in genres_list:
            for y in x:
                genres_text.append(y)

        genres_freq= Counter(genres_text)

        most_common_genre = str(genres_freq.most_common(1)[0][0])


    #Retrieving top Tracks details via GET request to top tracks endpoint
    top_tracks_url = user_top_items_url + 'tracks?' + urllib.parse.urlencode(request_params_tracks)
    tracks = requests.get(top_tracks_url, headers = headers)
    if tracks.status_code == 200:
        tracks = tracks.json()
        tracks = tracks['items']

        track_id = []
        tracks_key = []
        danceability = 0.0
        valence = 0.0
        instrumentalness = 0.0
        pitch_notation = {
                    0: 'C',
                    1: 'C#',
                    2: 'D',
                    3: 'D#',
                    4: 'E',
                    5: 'F',
                    6: 'F#',
                    7: 'G',
                    8: 'G#',
                    9: 'A',
                    10: 'A#',
                    11: 'B'
                }

        for track in tracks:
            id = track['id']
            track_id.append(id)


        for i in track_id:
            track_features_url = audio_features_url + str(i)
            track_features = requests.get(track_features_url, headers = headers)
            if track_features.status_code == 200:
                track_features = track_features.json()
                danceability = danceability + track_features['danceability']
                valence = valence + track_features['valence']
                instrumentalness = instrumentalness + track_features['instrumentalness']
                tracks_key.append(track_features['key'])

        avg_danceability = danceability/limit_tracks
        avg_valence = valence/limit_tracks
        avg_instrumentalness = instrumentalness/limit_tracks
        key_signature = statistics.mode(tracks_key)
        key_signature = pitch_notation[key_signature]

        return render_template('details.html', display_name = display_name, artists = artists, tracks = tracks, avg_danceability = avg_danceability, avg_valence = avg_valence, most_common_genre= most_common_genre.capitalize(), avg_instrumentalness = avg_instrumentalness, key_signature = key_signature)
    raise Exception(f'API Call to {user_top_items_url} failed')