"""
QUESTION:
Create a function `rate_movie` that allows users to rate movies from 1 to 5 stars and provide a comment. The function should take in user ID, movie ID, rating (1-5), and comment. It should also check if the user has added the movie to their favorites list and if they have already rated the movie. If the user has not added the movie to their favorites list, the function should return "Movie not in favorites list." If the user has already rated the movie, the function should return "User has already rated this movie." If the rating is successful, the function should return "Rating added successfully."
"""

def rate_movie(user_id, movie_id, rating, comment, user_ratings, user_favorites):
    """
    Allows users to rate movies from 1 to 5 stars and provide a comment.

    Args:
        user_id (int): The ID of the user.
        movie_id (int): The ID of the movie.
        rating (int): The rating of the movie (1-5).
        comment (str): The comment about the movie.
        user_ratings (dict): A dictionary of user ratings.
        user_favorites (dict): A dictionary of user favorites.

    Returns:
        str: A message indicating the result of the rating.
    """

    # Check if the user has added the movie to their favorites list
    if movie_id not in user_favorites.get(user_id, []):
        return "Movie not in favorites list."

    # Check if the user has already rated the movie
    if user_id in user_ratings and movie_id in user_ratings[user_id]:
        return "User has already rated this movie."

    # Validate the rating
    if not 1 <= rating <= 5:
        return "Invalid rating. Please rate between 1 and 5."

    # Add the rating and comment to the user's ratings
    if user_id not in user_ratings:
        user_ratings[user_id] = {}
    user_ratings[user_id][movie_id] = {"rating": rating, "comment": comment}

    return "Rating added successfully."