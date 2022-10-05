"""
import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state'


SPOTIPY_CLIENT_ID='f9d229f83fa2458c96e42648d255de2f'
SPOTIPY_CLIENT_SECRET='abed3f04d88641be84832777799a7e0c'
SPOTIPY_REDIRECT_URI='www.google.com'

try:
    token = util.prompt_for_user_token(username, scope)
except:
    os.remove(f'.cache-{username}')
    token = util.prompt_for_user_token(username, scope)


spotifyobject = spotipy.Spotify(auth = token)

devices = spotifyobject.devices()

def tracks():
    track = spotifyobject.current_user_playing_track()

    artist = track['item']['artists'][0]['name']
    track = track['item']['name']

    return (artist)

def user_info():
    user = spotifyobject.current_user()
    displayname = user['display_name']
    follower = user['followers']['total']

tracks()
"""

