"""
QUESTION:
Implement a function called `rate_movie` that allows a user to rate a movie with a rating from 1 to 10 stars and add a comment about the movie. The function should validate that the user has already added the movie to their favorites list and that they have not rated the movie before. The function should also ensure that the rating is within the valid range of 1 to 10.
"""

def rate_movie(user, movie, rating, comment):
    """
    Allows a user to rate a movie with a rating from 1 to 10 stars and add a comment about the movie.
    
    Args:
        user (dict): User's information, including their favorites list and ratings.
        movie (str): The title of the movie being rated.
        rating (int): The rating given to the movie, ranging from 1 to 10.
        comment (str): The comment provided by the user about the movie.
    
    Returns:
        bool: True if the rating was successful, False otherwise.
    """

    # Check if the user has already added the movie to their favorites list
    if movie not in user['favorites']:
        print("You must add the movie to your favorites list before rating it.")
        return False

    # Check if the user has already rated the movie before
    if movie in user['ratings']:
        print("You have already rated this movie.")
        return False

    # Validate that the rating is within the valid range of 1 to 10
    if rating < 1 or rating > 10:
        print("Rating must be between 1 and 10.")
        return False

    # Add the rating and comment to the user's ratings
    user['ratings'][movie] = {'rating': rating, 'comment': comment}
    
    # Return True to indicate a successful rating
    return True