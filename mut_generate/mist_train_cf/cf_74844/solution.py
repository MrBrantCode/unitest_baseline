"""
QUESTION:
Write a function named `streamed_movies` that takes three parameters: `movie_x`, `movie_y`, and `movie_z`, representing the names of movies X, Y, and Z respectively. The function should return a list of user IDs who have streamed movies X and Y but not Z. The database structure consists of three tables: `users` (user_id, username, email), `movies` (movie_id, movie_name), and `user_movies` (user_id, movie_id).
"""

def streamed_movies(movie_x, movie_y, movie_z, users, movies, user_movies):
    """
    Returns a list of user IDs who have streamed movies X and Y but not Z.

    Args:
    movie_x (str): The name of movie X.
    movie_y (str): The name of movie Y.
    movie_z (str): The name of movie Z.
    users (list of dictionaries): A list of user dictionaries with 'user_id' key.
    movies (list of dictionaries): A list of movie dictionaries with 'movie_id' and 'movie_name' keys.
    user_movies (list of dictionaries): A list of user-movie dictionaries with 'user_id' and 'movie_id' keys.

    Returns:
    list of integers: A list of user IDs who have streamed movies X and Y but not Z.
    """
    # Get the movie IDs for movies X, Y, and Z
    movie_x_id = next((movie['movie_id'] for movie in movies if movie['movie_name'] == movie_x), None)
    movie_y_id = next((movie['movie_id'] for movie in movies if movie['movie_name'] == movie_y), None)
    movie_z_id = next((movie['movie_id'] for movie in movies if movie['movie_name'] == movie_z), None)

    # Get the user IDs who have streamed movies X and Y
    users_streamed_xy = set(user['user_id'] for user in users for user_movie in user_movies 
                            if user['user_id'] == user_movie['user_id'] and 
                            (user_movie['movie_id'] == movie_x_id or user_movie['movie_id'] == movie_y_id))

    # Get the user IDs who have streamed movie Z
    users_streamed_z = set(user['user_id'] for user in users for user_movie in user_movies 
                           if user['user_id'] == user_movie['user_id'] and user_movie['movie_id'] == movie_z_id)

    # Return the user IDs who have streamed movies X and Y but not Z
    return list(users_streamed_xy - users_streamed_z)