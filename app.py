from flask import Flask, render_template, request, redirect, url_for
import os
import random
from songs import resp, artists_resp
from lyrics import lyrics_resp
from user_song import user_song_resp

def rand_artists():
    random_number = random.randint(0,2)
    artists = ['0OpWIlokQeE7BNQMhuu2Nx', '7dGJo4pcD2V6oG8kP0tJRR', '137W8MRPWKqSmrBGDBFSop'] #colt, eninem, wiz
    return artists[random_number]

def get_Lyrics(song_name, song_artists):
    data = lyrics_resp(song_name, song_artists)
    length = len(data["response"]["hits"])
    try:
        left_perm = song_name.index('(')
        right_perm = song_name.index(')')
        song_name = song_name[0:left_perm] + song_name[right_perm:-1]
    except ValueError:
        song_name=song_name

    for i in range(0, length):
        if(data["response"]["hits"][i]["result"]["title"] == song_name):
            return data["response"]["hits"][i]["result"]["url"]
    return data["response"]["hits"][0]["result"]["url"]

def rand_song():
    artists = rand_artists()

    data = resp(artists)
    artists_data = artists_resp(artists)

    length = len(data['tracks'])
    random_number = random.randint(0,length-1)

    name = data['tracks'][random_number]['name']
    artists = data['tracks'][random_number]['album']['artists'][0]['name']
    lyrics = get_Lyrics(name, artists)
    return { 'name': name,
                'artists': artists,
                'artists_img': artists_data['images'][0]['url'],
                'image': data['tracks'][random_number]['album']['images'][0]['url'],
                'song_preview_url': data['tracks'][random_number]['preview_url'],
                'song_lyrics': lyrics
            }

def user_song(tag):
    data = user_song_resp(tag)
    name = data['tracks']['items'][0]['name']
    artists = data['tracks']['items'][0]['album']['artists'][0]['name']
    artists_data = artists_resp(data['tracks']['items'][0]['album']['artists'][0]['id'])
    lyrics = get_Lyrics(name, artists)
    return { 'name': name,
                'artists': artists,
                'artists_img': artists_data['images'][0]['url'],
                'image': data['tracks']['items'][0]['album']['images'][0]['url'],
                'song_preview_url': data['tracks']['items'][0]['preview_url'],
                'song_lyrics': lyrics
            }

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        tag = request.form['tag']
        if(tag == ""):
            data=rand_song()
        else:
            data = user_song(tag)
    else:
        data=rand_song()
    return render_template('index.html', data=data)

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv("IP", '0.0.0.0'),
    debug=True
)