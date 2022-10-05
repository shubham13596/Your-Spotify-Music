import os

class Config(object):
    """Flask base config, specifies general settings."""

    SESSION_TYPE = "filesystem"
    SESSION_FILE_DIR = "./.flask_session/"
    SECRET_KEY = os.environ.get("SECRET_SESSION_KEY")

    # SPOTIFY
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")


class ProductionConfig(Config):
    """Flask production config, making sure all is set for dev env."""

    TESTING = False
    DEBUG = False
    SHOW_DIALOG = False
    FLASK_ENV = "production"
    REDIRECT_URI = "https://your-spotify-music.herokuapp.com/callback"


class DevelopmentConfig(Config):
    """Flask development config, such that we can debug."""

    TESTING = True
    DEBUG = True
    SHOW_DIALOG = True
    FLASK_ENV = "development"
    REDIRECT_URI = "https://shubham13596-code50-102696888-x5q94g56qcv5jq-5000.githubpreview.dev/callback"


# API_BASE = "https://accounts.spotify.com"

# Old redirect uri's:
# REDIRECT_URI = "https://spodivide.herokuapp.com/login"
# REDIRECT_URI = "https://spodivide.com/login"
# Make sure you add this to Redirect URIs in the setting of the application dashboard of Spotify developee