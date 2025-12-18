"""
QUESTION:
Implement a function `get_movie_recommendations` that takes a list of user's favorite movies, their search history, and a dictionary of movie genres as input, and returns a list of personalized movie recommendations based on the given data.
"""

def get_movie_recommendations(user_favorite_movies, user_search_history, movie_genres):
    """
    This function takes a list of user's favorite movies, their search history, 
    and a dictionary of movie genres as input, and returns a list of personalized 
    movie recommendations based on the given data.

    Parameters:
    user_favorite_movies (list): A list of user's favorite movies.
    user_search_history (list): A list of user's search history.
    movie_genres (dict): A dictionary of movie genres.

    Returns:
    list: A list of personalized movie recommendations.
    """

    # Combine user's favorite movies and search history into a single list
    user_data = user_favorite_movies + user_search_history

    # Initialize an empty dictionary to store movie genres count
    genres_count = {}

    # Iterate over user's data to count the occurrences of each genre
    for movie in user_data:
        if movie in movie_genres:
            genre = movie_genres[movie]
            if genre in genres_count:
                genres_count[genre] += 1
            else:
                genres_count[genre] = 1

    # Sort genres by their count in descending order
    sorted_genres = sorted(genres_count, key=genres_count.get, reverse=True)

    # Initialize an empty list to store recommended movies
    recommended_movies = []

    # Iterate over sorted genres to get recommended movies
    for genre in sorted_genres:
        for movie, movie_genre in movie_genres.items():
            if movie_genre == genre and movie not in user_data:
                recommended_movies.append(movie)
                break

    return recommended_movies