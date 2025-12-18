"""
QUESTION:
Write a function `create_recommended_user_list` that generates a list of recommended users for a given user based on their interests. The function should take two parameters: `user_id` and `user_interests`. It should return a list of user IDs that have at least one matching interest. The function should be efficient enough to handle a large number of users and interests.
"""

def create_recommended_user_list(user_id, user_interests, all_users):
    """
    This function generates a list of recommended users for a given user based on their interests.

    Args:
        user_id (int): The ID of the user for whom we want to generate recommendations.
        user_interests (list): A list of interests of the user.
        all_users (dict): A dictionary containing all users and their interests.

    Returns:
        list: A list of user IDs that have at least one matching interest with the given user.
    """

    # Initialize an empty set to store recommended user IDs
    recommended_users = set()

    # Iterate over each user in the all_users dictionary
    for current_user, interests in all_users.items():
        # Skip the current user if it's the same as the given user
        if current_user == user_id:
            continue

        # Check if there are any common interests between the current user and the given user
        if set(interests) & set(user_interests):
            # Add the current user to the recommended_users set
            recommended_users.add(current_user)

    # Return the list of recommended user IDs
    return list(recommended_users)