"""
QUESTION:
Create a function named `recommend_movies` that takes a dictionary of user ratings for movies, where each key is a user ID and each value is another dictionary with movie IDs as keys and ratings as values. The function should use collaborative filtering to recommend movies to a given user.
"""

def recommend_movies(user_ratings, target_user_id, num_recommendations=5):
    """
    Recommends movies to a given user based on collaborative filtering.

    Args:
    user_ratings (dict): A dictionary of user ratings for movies.
    target_user_id (str): The ID of the user for whom to make recommendations.
    num_recommendations (int, optional): The number of recommendations to make. Defaults to 5.

    Returns:
    list: A list of recommended movie IDs.
    """

    # Create a dictionary to store the similarity between users
    similarities = {}
    
    # Calculate the similarity between the target user and every other user
    for user_id, ratings in user_ratings.items():
        if user_id != target_user_id:
            similarity = calculate_similarity(user_ratings[target_user_id], ratings)
            similarities[user_id] = similarity
    
    # Find the users with the highest similarity to the target user
    similar_users = sorted(similarities, key=similarities.get, reverse=True)[:num_recommendations]
    
    # Get the movies rated by the similar users
    recommended_movies = set()
    for user_id in similar_users:
        for movie_id, rating in user_ratings[user_id].items():
            if movie_id not in user_ratings[target_user_id]:
                recommended_movies.add((movie_id, rating))
    
    # Sort the recommended movies by rating and return the top N
    recommended_movies = sorted(recommended_movies, key=lambda x: x[1], reverse=True)[:num_recommendations]
    return [movie_id for movie_id, rating in recommended_movies]


def calculate_similarity(ratings1, ratings2):
    """
    Calculates the similarity between two sets of ratings.

    Args:
    ratings1 (dict): The first set of ratings.
    ratings2 (dict): The second set of ratings.

    Returns:
    float: The similarity between the two sets of ratings.
    """

    # Calculate the dot product of the two sets of ratings
    dot_product = sum(ratings1.get(movie_id, 0) * ratings2.get(movie_id, 0) for movie_id in set(ratings1) | set(ratings2))
    
    # Calculate the magnitude of each set of ratings
    magnitude1 = sum(rating ** 2 for rating in ratings1.values()) ** 0.5
    magnitude2 = sum(rating ** 2 for rating in ratings2.values()) ** 0.5
    
    # Calculate the cosine similarity
    similarity = dot_product / (magnitude1 * magnitude2)
    return similarity