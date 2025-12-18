"""
QUESTION:
Create a function `rank_movies(movies)` that takes a dictionary `movies` where the keys are movie identifiers and the values are lists of user ratings. The function should return a list of movie identifiers in descending order of average rating. If two movies have the same average rating, they should be ordered based on their identifiers in ascending order.
"""

def rank_movies(movies):
    avg_ratings = {movie: sum(ratings) / len(ratings) for movie, ratings in movies.items()}
    sorted_movies = sorted(avg_ratings.items(), key=lambda x: (-x[1], x[0]))
    return [movie[0] for movie in sorted_movies]