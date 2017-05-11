[![Documentation Status](https://readthedocs.org/projects/pymoe/badge/?version=latest)](http://pymoe.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/ccubed/PyMoe.svg?branch=master)](https://travis-ci.org/ccubed/PyMoe)
# PyMoe
Welcome to PyMoe, the only python lib you'll ever need if you need the animu/mangu on the python platform.
You have found async PyMoe. It's all the goodness of PyMoe, but you know, Async.
Please note that I do not support 3.4. If you want to use async, update to 3.5+.

The Async version of PyMoe will sucessfully propogate whatever event loop you 
give it. This could be uvloop or the built in asyncio event loop. If one isn't
given then asyncio.get_event_loop is used.

# Async Conversion Status
## Overall
0 of 6 Done
## Summary
* Kitsu: Not Done
* Bakatsuki: Not Done
* Mal: Not Done
* VNDB: Not Done
* AniDB: Not Done
* Anilist: Not Done

## Kitsu
Ready to use as of version 0.8.
Kitsu is the new Hummingbird if you're wondering where Hummingbird went.

## A note on SearchWrapper
You should be aware that SearchWrapper is now an AsyncIterator. Meaning that
while you can still use the old next() method, you should now be using async 
for!

## Instances
To create an instance do:
```python
from Pymoe import Kitsu
instance = Kitsu(client_id, client_secret)
```
You can get the client_id and client_secret off the forums. There's only one.
You have six interfaces: anime, manga, drama, auth, user, library
```python
await instance.anime.get(id)  # Search anime by ID
await instance.anime.search(term)  # Search anime by term.
await instance.manga.get(id)  # Search manga by ID
await instance.manga.search(term)  # Search manga by term
await instance.drama.get(id)  # Search drama by ID
await instance.drama.search(term)  # Search drama by term
await instance.auth.authenticate(username, password)  # Authenticate through oauth
await instance.user.search(term)  # Search for users by name
await instance.user.get(id)  # Search for user by ID
await instance.user.update(id, dictionary, token)  # Update a user's attributes
await instance.user.create(dictionary)  # Create a new user. I haven't tested this.
await instance.library.get(id)  # Get a user's library entries (lol, see source notes)
```

## Anidb
Status: Not Started

## Anilist
Status: Not Started

## Bakatsuki
Status: Finished as of 0.2
To create an instance do:
```python
from Pymoe import Bakatsuki
instance = Bakatsuki()
```
From there you can get information on Bakatsuki's projects.
Keep in mind that whenever a list is returned, it's a list of tuples in the
order (pageid, title).
```python
await instance.active()  # Get a list of active projects
await instance.chapters(title)  # return the chapters for a title
await instance.get_text(title)  # return the text of a given page
await instance.light_novels(language)  # Get a list of language's light novels
await instance.teaser(language)  # Get a list of language's teaser projects
await instance.web_novels(language)  # Get a list of language's web novels
```

## Mal
Status: Finished as of 0.3
To create an instance.
```python
from Pymoe import Mal
instance = Mal(username, password)  # Since every endpoint requires authentication, un/pw isn't optional
```
This particular branch relies on a ton of abstractions and encapsulations. You should read up on them. However, ultimately, it makes your life as a programmer easier. Anime and Manga share the same 4 functions: search, add, update, delete.
```python
await instance.anime.search(term)  # Return a list of Anime objects
await instance.manga.search(term)  # Return a list of Manga objects
await instance.anime.update(Pymoe.Mal.Objects.Anime)  # Update a user's list with the given anime data
await instance.manga.delete(Pymoe.Mal.Objects.Manga)  # Delete this manga from the user's list
await instance.anime.add(Pymoe.Mal.Objects.Anime)  # Add the anime to the user's list
await instance.user(username)  # Return a user object that contains user stats and a full anime, manga list
```

## VNDB
Status: Finished as of 0.7 Beta
To create an instance.
```python
from Pymoe import Vndb
instance = Vndb(username, password)  # Username and password are optional, but allow you to login as a user
```
This allows you access to some of the VNDB database. Currently it's just the querying part.
```python
await instance.dbstats()  # Return the list of Database stats as seen on the homepage
await instance.get(stype, flags, filters, options)  # Query the DB. You have to read the VNDB API Docs and my Docs for this. No way around it. Their API is complicated.
await instance.set(stype, sid, fields) # Modify the DB. See the API docs. This is for VNLists, Wishlists and Votelists.
```
