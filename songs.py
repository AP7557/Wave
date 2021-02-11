from auth import access_token
import requests

# JSON object
new_release = 'https://api.spotify.com/v1/artists/'

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token),
}

params = {
    'market': 'US'
}

def resp(id):
    response = requests.get(new_release + id +'/top-tracks', params=params, headers=headers)
    return response.json()

def artists_resp(id):
    response = requests.get(new_release + id +'/top-tracks', params=params, headers=headers)
    return response.json()