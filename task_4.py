# Find the longest movie by genre
# Develop a function called longest_movie_by_genre that identifies the movie with the longest running time within a specific genre. The function should accept the genre as the first argument and the movie list as the second argument.


from data import movies
from pprint import pprint

def longest_movie(movies):
    longest_movie_variable = movies[0]
    for movie in movies:
        if movie["runtime"] > longest_movie_variable["runtime"]:
            longest_movie_variable = movie

        
    return longest_movie_variable

def longest_movie_by_genre(genre, movies):
    movies_by_genre = []

    for movie in movies: 
        if genre in movie["genres"]:
            movies_by_genre.append(movie)

    return longest_movie(movies_by_genre)

pprint(longest_movie_by_genre("Comedy", movies))