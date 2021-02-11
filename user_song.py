from auth import access_token
import requests

# JSON object
user_url = 'https://api.spotify.com/v1/search'

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token),
}

def user_song_resp(song):
    response = requests.get(user_url, params= {'q': song, 'type': 'track'}, headers=headers)
    return response.json()