import spotipy
import spotipy.util as util
import textwrap

from inky import InkyPHAT

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_fredoka_one import FredokaOne
from font_source_sans_pro import SourceSansPro

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

font0 = ImageFont.truetype(FredokaOne, 16)
font1 = ImageFont.truetype(FredokaOne, 22)
font2 = ImageFont.truetype(FredokaOne, 18)

if current_track == None:

    message = "Not Playing :("
    w, h = font1.getsize(message)
    x = 5
    #x = inky_display.WIDTH / 20
    y = (inky_display.HEIGHT / 7)*3 - (h / 2)

    draw.text((x, y), message, inky_display.RED, font1)

else:
    song_name = current_track['item']['name']
    song_artist = current_track['item']['artists'][0]['name']

    message0 = "Now Playing"
    w0, h0 = font0.getsize(message0)
    x0 = 5
    #x0 = inky_display.WIDTH / 20
    y0 = (inky_display.HEIGHT / 6) - (h0 / 2)

    message1 = song_artist
    w1, h1 = font1.getsize(message1)
    x1 = 5
    #x1 = inky_display.WIDTH / 2 - (w1 / 2)
    y1 = (inky_display.HEIGHT / 7)*3 - (h1 / 2) - 1

    message2 = textwrap.fill(song_name, 21)
    w2, h2 = font2.getsize(message2)
    x2 = 5
    #x2 = inky_display.WIDTH / 2 - (w2 / 2)
    y2 = (inky_display.HEIGHT / 3)*2 - (h2 / 2)

    #still to fix :(
    #img = Image.open("Stupify.png")
    #draw = ImageDraw.Draw(img)

    draw.text((x0, y0), message0, inky_display.BLACK, font0)
    draw.text((x1, y1), message1, inky_display.RED, font1)
    draw.text((x2, y2), message2, inky_display.RED, font2)

flipped = img.rotate(180)
inky_display.set_image(flipped)
inky_display.show()