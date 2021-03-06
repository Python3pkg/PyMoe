[![Documentation Status](https://readthedocs.org/projects/pymoe/badge/?version=latest)](http://pymoe.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/ccubed/PyMoe.svg?branch=master)](https://travis-ci.org/ccubed/PyMoe)
# PyMoe
Welcome to PyMoe, the only python lib you'll ever need if you need the animu/mangu on the python platform.

## Kitsu
Ready to use as of version 0.8.
Kitsu is the new Hummingbird if you're wondering where Hummingbird went.
To create an instance do:
```python
from Pymoe import Kitsu
instance = Kitsu(client_id, client_secret)
```
You can get the client_id and client_secret off the forums. There's only one.
You have six interfaces: anime, manga, drama, auth, user, library
```python
instance.anime.get(id)  # Search anime by ID
instance.anime.search(term)  # Search anime by term
instance.manga.get(id)  # Search manga by ID
instance.manga.search(term)  # Search manga by term
instance.drama.get(id)  # Search drama by ID
instance.drama.search(term)  # Search drama by term
instance.auth.authenticate(username, password)  # Authenticate through oauth
instance.user.search(term)  # Search for users by name
instance.user.get(id)  # Search for user by ID
instance.user.update(id, dictionary, token)  # Update a user's attributes
instance.user.create(dictionary)  # Create a new user. I haven't tested this.
instance.library.get(id)  # Get a user's library entries (lol, see source notes)
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
```python
instance.active()  # Return a tuple containing (title, pageid) of active projects
instance.chapters(title)  # return the chapters for a title
instance.get_text(title)  # return the text of a given page
instance.light_novels(language)  # Get a list of language's light novels
instance.teaser(language)  # Get a list of language's teaser projects
instance.web_novels(language)  # Get a list of language's web novels
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
instance.anime.search(term)  # Return a list of Anime objects
instance.manga.search(term)  # Return a list of Manga objects
instance.anime.update(Pymoe.Mal.Objects.Anime)  # Update a user's list with the given anime data
instance.manga.delete(Pymoe.Mal.Objects.Manga)  # Delete this manga from the user's list
instance.anime.add(Pymoe.Mal.Objects.Anime)  # Add the anime to the user's list
instance.user(username)  # Return a user object that contains user stats and a full anime, manga list
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
instance.dbstats()  # Return the list of Database stats as seen on the homepage
instance.get(stype, flags, filters, options)  # Query the DB. You have to read the VNDB API Docs and my Docs for this. No way around it. Their API is complicated.
instance.set(stype, sid, fields) # Modify the DB. See the API docs. This is for VNLists, Wishlists and Votelists.
```
