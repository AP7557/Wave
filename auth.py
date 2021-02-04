import os
from dotenv  import load_dotenv, find_dotenv
import requests

# access token
load_dotenv(find_dotenv())

url = "https://accounts.spotify.com/api/token"

token = requests.post(url, {
    'grant_type': 'client_credentials',
    'client_id': os.getenv("CLIENT_ID"),
    'client_secret': os.getenv('CLIENT_SECRET'),
})

token_data = token.json()

access_token = token_data['access_token']