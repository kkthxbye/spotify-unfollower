__version__ = '0.1.0'

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotify_unfollower.utils import grouper

scope = 'user-follow-read user-follow-modify'

spotify = Spotify(auth_manager=SpotifyOAuth(scope=scope))

page_length = 50
offset = 0

cum = {}

while True:
    response = spotify.current_user_followed_artists(
        limit=page_length,
        after=offset,
    )
    artists = response.get('artists', {})
    items = artists.get('items', [])
    cum.update({x['id']: x['name'] for x in items})
    print(f'Collected {len(cum)} records of {artists.get("total")}')
    offset += page_length

    if not items:
        break

for chunk in grouper(cum.items(), 10):
    print(f'Unfollowing: {", ".join(x[1] for x in chunk)}')
    resp = spotify.user_unfollow_artists(x[0] for x in chunk)
    print(resp)
