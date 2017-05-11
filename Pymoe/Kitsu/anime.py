import aiohttp
from ..errors import *
from .helpers import SearchWrapper


class KitsuAnime:
    def __init__(self, loop, session, api, header):
        self.eloop = loop
        self.apiurl = api
        self.header = header
        self.session = session

    async def get(self, aid):
        """
        Get anime information by id.

        :param int aid: ID of the anime.
        :return: Dictionary or None (for not found)
        :rtype: Dictionary or None
        :raises: :class:`Pymoe.errors.ServerError`
        """
        async with self.session() as session:
            async with session.get(self.apiurl + "/anime/{}".format(aid), headers=self.header) as r:
                if r.status != 200:
                    if r.status == 404:
                        return None
                    else:
                        raise ServerError
            
                return await r.json()

    async def search(self, term):
        """
        Search for anime by term.

        :param str term: What to search for.
        :return: The results as a SearchWrapper iterator.
        :rtype: SearchWrapper
        """
        async with self.session() as session:
            async with session.get(self.apiurl + "/anime", params={"filter[text]": term}, headers=self.header) as r:
                if r.status != 200:
                    raise ServerError
                    
                jsd = await r.json()
                
                if jsd['meta']['count']:
                    return SearchWrapper(jsd['data'], jsd['links']['next'] if 'next' in jsd['links'] else None, self.header)
                else: 
                    return None
