""" import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_SECRET = os.getenv('SECRET_KEY')
CLIENT_ID = os.getenv('CLIENT_ID')
REDIRECT_URI =os.getenv('REDIRECT_URI')
"""

import os

class Config:
    CLIENT_SECRET = os.getenv("SECRET_KEY")
    CLIENT_ID = os.getenv("CLIENT_ID")
    REDIRECT_URI = os.getenv("REDIRECT_URI")