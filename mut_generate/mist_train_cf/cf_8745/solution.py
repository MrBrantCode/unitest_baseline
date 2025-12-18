"""
QUESTION:
Write a function `get_highly_rated_movies` to retrieve movie information. The function should return a list of movies with a rating above 7.5, released in the year 2000, and a runtime of at least 120 minutes. The result should include the title, rounded rating to the nearest decimal point, release year, and genre of each movie. The movies should be sorted in descending order by rating and then by title in ascending order.
"""

def get_highly_rated_movies(movies):
    highly_rated_movies = [
        {
            'title': movie['title'],
            'rounded_rating': round(movie['rating'], 1),
            'release_year': movie['release_year'],
            'genre': movie['genre']
        }
        for movie in movies
        if movie['rating'] > 7.5
        and movie['release_year'] == 2000
        and movie['runtime'] >= 120
    ]

    highly_rated_movies.sort(key=lambda x: (-x['rounded_rating'], x['title']))

    return highly_rated_movies