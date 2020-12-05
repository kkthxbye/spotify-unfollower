from typing import Callable, Dict, Generator

from spotify_unfollower.logger import create_logger

logger = create_logger(__name__)


def spotify_pagination_generator(
    spotipy_call: Callable[..., Dict],
    unwrap: Callable[[Dict], Dict],
    page_size: int = 50,
) -> Generator[Dict, None, None]:
    offset = 0
    while True:
        page_content = spotipy_call(limit=page_size, offset=offset)
        items = page_content.get('items', [])
        yield from (unwrap(x) for x in items)
        logger.debug('Received page %s (%s items)', offset // page_size, len(items))
        offset += page_size
        total = page_content.get('total')
        if offset >= total:
            break
