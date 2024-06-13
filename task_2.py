# Search for movies by genre
# Create a function called find_by_genre that returns a list of movie titles that match a specific genre. The function should accept two arguments: the genre to search for and a list of movies.


from pprint import pprint
from data import movies 

def find_by_genre(genre, movies): 
    movie_list = []
    for movie in movies: 
        if genre in movie["genres"]:
            movie_list.append(movie["title"])
    return movie_list
    
genre = "Comedy" 

pprint(find_by_genre(genre, movies))