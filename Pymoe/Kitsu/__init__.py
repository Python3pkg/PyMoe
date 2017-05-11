import asyncio
import aiohttp
from .anime import *
from .user import *
from .library import *
from .manga import *
from .drama import *
from .auth import *


class Kitsu:
    """
        :ivar KitsuAnime anime: Instance interface for the Kitsu Anime endpoints
        :ivar KitsuUser user: Instance interface for the Kitsu User endpoints
        :ivar KitsuLib library: Instance interface for the Kitsu Library endpoints.
        :ivar KitsuManga manga: Instance interface for the Kitsu Manga endpoints.
        :ivar KitsuDrama drama: Instance interface for the Kitsu Drama endpoints.
        :ivar KitsuAuth auth: Instance interface for the Kitsu Auth endpoints / storage engine.
    """
    def __init__(self, loop=None, cid, csecret):
        """
        Initialize a new Kitsu API instance.
        """
        api = "https://kitsu.io/api/edge"
        header = {
            'User-Agent': 'Pymoe (git.vertinext.com/ccubed/Pymoe)',
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json'
        }
        our_loop = loop if loop is not None else asyncio.get_event_loop()
        our_session = aiohttp.ClientSession(loop=our_loop)
        self.anime = KitsuAnime(our_loop, our_session, api, header)
        self.manga = KitsuManga(our_loop, our_session, api, header)
        self.drama = KitsuDrama(our_loop, our_session, api, header)
        self.library = KitsuLib(our_loop, our_session, api, header)
        self.user = KitsuUser(our_loop, our_session, api, header)
        self.auth = KitsuAuth(our_loop, our_session, header, cid, csecret)
