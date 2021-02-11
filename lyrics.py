from auth import lyrics_access_token
import requests

# JSON object
lyrics_url = 'https://api.genius.com/search?q='

headers = {
    'Authorization': 'Bearer {token}'.format(token=lyrics_access_token),
}

def lyrics_resp(song_name, song_artists):
    response = requests.get(lyrics_url + song_name + " by " + song_artists, headers=headers)
    return response.json()


