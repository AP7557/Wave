from flask import Flask, render_template
import os
import random

app = Flask(__name__)
# load_dotenv(find_dotenv())
@app.route('/')
def hello_world():
    random_number = random.randint(0,3)
    artists = ['0OpWIlokQeE7BNQMhuu2Nx', '7dGJo4pcD2V6oG8kP0tJRR', '137W8MRPWKqSmrBGDBFSop'] #colt, eninem, wiz
    return render_template('index.html')

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv("IP", '0.0.0.0'),
    debug=True
)