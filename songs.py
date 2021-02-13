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

#Return random song for the artist json data
def resp(id):
    response = requests.get(new_release + id +'/top-tracks', params=params, headers=headers)
    return response.json()

#Return artist json data
def artists_resp(id):
    response = requests.get(new_release + id, params=params, headers=headers)
    return response.json()