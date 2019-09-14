# Stupify
Spotify Now Playing Inky pHat Badge
<br><br>
## Requirements
 
### Spotipy
```
pip3 spotipy
pip3 install git+https://github.com/plamere/spotipy.git --upgrade
```
### Inky 
``` 
curl https://get.pimoroni.com/inky | bash
```
or ```sudo pip3 install inky``` (didn't work for me, hung at numpy)
<br><br>
## Configuration
### Stupify.py
Pull current user playing track from Spotify Web API.
Render result to Inky pHat

### now.py
Same as Stupify but without the Inky pHat output.
<br><br>
## Todo:
MQTT integration

## Reference
[Old version on pip/easy_install installation #211](https://github.com/plamere/spotipy/issues/211)