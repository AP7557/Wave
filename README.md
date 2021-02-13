# Wave
Wave is an app that allows users to browse music from the [The Spotify API].

## Requirements and RUN
1. `pip install -r requirements.txt`
2. `Run command in terminal (in your project directory): python app.py`

###Additional Required Files
1. `Create a .env file`
2. `Create Spotify developer account to get the Client Id and Client Secret and put it in the file`
3. `Create Genius account to get the Access Token`

- [x] Randomly chose a music artist from a given list of 3.
- [x] Fetch top 10 track of that artist.
- [x] Randomly choose a song and show (song name, song artist, song-related image, song preview URL).
- [x] Clickable link for user to go to the song's lyrics page.

### BONUS
- [x] User can search a music artist from the Spotify API.
- [ ] Play the full song.

## Question and Answer
1. What are at least 3 technical issues you encountered with your project? How did you fix them?
- The very first issuse I came across with was my styling was not getting loaded when I change them, I had to fix it by renaming the file everytime
- The Spotify API documentation was hard to follow to get the access token, I had to search on the web on how to get the token
- The Genius API to get Access Token was hard to understand, took some help for fellow friends


2. What are known problems, if any, with your project?
- The project looks to plain, and when reloading the page it doesn't change the POST method back to GET

3. What would you do to improve your project in the future?
- Instead of playing the preview of the song, I might play the whole song or make a link that takes you to that sone page, maybe even add a search functionality for songs

## APIs used
- [Spotify API](https://developer.spotify.com) - For music artists and its song
- [Genius API](https://docs.genius.com/#/getting-started-h1) - Get lyrics

## Framework used
- [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) - Different endpoint for web application

## Libraries used
- [os](https://docs.python.org/3/library/os.html) - Operating system dependent functionality
- [random](https://docs.python.org/3/library/random.html) - Number generator
- [requests](https://requests.readthedocs.io/en/master/) - HTTP library to fetch data
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Adds .env to safely store api keys

## Technology used
- [AWS-Cloud9](https://aws.amazon.com/cloud9/) - Online IDE for write, run, and debug serverless applications