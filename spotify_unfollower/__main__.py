from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

from spotify_unfollower.generators import spotify_pagination_generator
from spotify_unfollower.logger import create_logger
from spotify_unfollower.utils import grouper

logger = create_logger(__name__)

page_size = 50

scope = ' '.join([
    'user-follow-read',
    'user-follow-modify',
    'user-library-read',
    'user-library-modify',
])

spotify = Spotify(auth_manager=SpotifyOAuth(scope=scope))

for chunk in grouper(
        iterable=list(spotify_pagination_generator(
            spotipy_call=spotify.current_user_saved_albums,
            unwrap=lambda x: x.get('album'),
            page_size=page_size,
        )),
        n=page_size,
):
    albums = list(chunk)
    logger.debug('Unfollowing \n%s', '\n'.join([
        str((x.get('id'), x.get('name'))) for x in albums
    ]))
    spotify.current_user_saved_albums_delete(album.get('id') for album in albums)
