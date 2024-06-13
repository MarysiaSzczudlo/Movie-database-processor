# Find the category: Drama
# Create a function called dramas that takes a list of movies as an argument. This function should return a new list containing the titles of movies whose genre includes "Drama".

from pprint import pprint
from data import movies 

def dramas(movies):
    result=[]

    for movie in movies:
        if "Drama" in movie["genres"]:
            # funkcja, która dodaje coś do listy to append
            result.append(movie["title"])


    return result

pprint(dramas(movies))