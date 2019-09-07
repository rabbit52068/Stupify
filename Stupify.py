import spotipy
import spotipy.util as util

from inky import InkyPHAT

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_fredoka_one import FredokaOne

CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
USERNAME = "your_username"

REDIRECT_URI = "call_back_url"
#REDIRECT_URI = "http://localhost:8888/callback"

scope = 'user-read-currently-playing'
# scope = 'user-read-playback-state'
# works as well

token = util.prompt_for_user_token(username, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)

spotify = spotipy.Spotify(auth=token)
current_track = spotify.current_user_playing_track()

now_font = ImageFont.truetype(FredokaOne, 16)
font = ImageFont.truetype(FredokaOne, 22)
font2 = ImageFont.truetype(FredokaOne, 18)

if current_track == None:

    message = "Not Playing :("
    w, h = font.getsize(message)
    x = 5
    #x = inky_display.WIDTH / 20
    y = (inky_display.HEIGHT / 7)*3 - (h / 2)

    draw.text((x, y), message, inky_display.RED, font)
    inky_display.set_image(img)
    inky_display.show()

else:
    song_name = current_track['item']['name']
    song_artist = current_track['item']['artists'][0]['name']

    now_playing = "Now Playing"
    nw, nh = font.getsize(now_playing)
    now_x = 5
    #now_x = inky_display.WIDTH / 20
    now_y = (inky_display.HEIGHT / 5) - (nh / 2)

    message = song_artist
    w, h = font.getsize(message)
    x = 5
    #x = inky_display.WIDTH / 20
    y = (inky_display.HEIGHT / 7)*3 - (h / 2)

    message2 = song_name
    w2, h2 = font.getsize(message2)
    x2 = 5
    #x2 = inky_display.WIDTH / 20
    y2 = (inky_display.HEIGHT / 3)*2 - (h2 / 2)

    #img = Image.open("Stupify.png")
    #draw = ImageDraw.Draw(img)

    draw.text((now_x, now_y), now_playing, inky_display.BLACK, now_font)
    draw.text((x, y), message, inky_display.RED, font)
    draw.text((x2, y2), message2, inky_display.RED, font2)
    inky_display.set_image(img)
    inky_display.show()