"""
QUESTION:
Create a function called `top_three_users` that takes a JSON object containing a list of users with 'name' and 'score' attributes. The function should return the names of the top three users with the highest scores in descending order.
"""

import json

def top_three_users(json_data):
    """
    This function takes a JSON object containing a list of users with 'name' and 'score' attributes.
    It returns the names of the top three users with the highest scores in descending order.

    Args:
        json_data (str): A JSON object containing a list of users.

    Returns:
        list: A list of names of the top three users with the highest scores.
    """
    data = json.loads(json_data)
    users = data.get("users", [])
    sorted_users = sorted(users, key=lambda user: user.get("score", 0), reverse=True)
    return [user.get("name", "") for user in sorted_users[:3]]