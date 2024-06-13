# Find the longest movie
# Create a function called longest_movie that determines the movie with the longest duration from the list of movies provided as an argument.


from data import movies


def longest_movie(movies):
    longest_movie_variable = movies[0]
    for movie in movies:
        if movie["runtime"] > longest_movie_variable["runtime"]:
            longest_movie_variable = movie

        
    return longest_movie_variable

zmienna = longest_movie(movies)

print(f"The longest movie is: '{zmienna["title"]}'") 


    
