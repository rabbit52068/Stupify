import spotipy
import spotipy.util as util

CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
USERNAME = "your_username"

REDIRECT_URI = "call_back_url"
#REDIRECT_URI = "http://localhost:8888/callback"

scope = 'user-read-currently-playing'
# scope = 'user-read-playback-state'
# works as well

token = util.prompt_for_user_token(USERNAME, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)

spotify = spotipy.Spotify(auth=token)
current_track = spotify.current_user_playing_track()

if current_track == None:
  print("Not Playing")
else:
  #print(current_track)
  song_name = current_track['item']['name']
  song_artist = current_track['item']['artists'][0]['name']
  print("Now playing {} by {}".format(song_name, song_artist))