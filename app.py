from flask import Flask, render_template
import os
import random
from songs import resp

def rand_artists():
    random_number = random.randint(0,2)
    artists = ['0OpWIlokQeE7BNQMhuu2Nx', '7dGJo4pcD2V6oG8kP0tJRR', '137W8MRPWKqSmrBGDBFSop'] #colt, eninem, wiz
    return artists[random_number]

def rand_song():
    data = resp(rand_artists())
    length = len(data['tracks'])
    random_number = random.randint(0,length-1)
    return data['tracks'][random_number]['name']

print(rand_song())
# app = Flask(__name__)
# # load_dotenv(find_dotenv())
# @app.route('/')
# def hello_world():
#
#     return render_template('index.html')

# app.run(
#     port=int(os.getenv('PORT', 8080)),
#     host=os.getenv("IP", '0.0.0.0'),
#     debug=True
# )