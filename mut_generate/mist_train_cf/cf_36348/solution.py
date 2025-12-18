"""
QUESTION:
Implement a point-based system for a social media platform with the following conditions:

- Define a method `earn_points` that allows users to earn points by engaging with the platform.
- Define a method `use_points` that allows users to use their points to perform certain actions.
- Define a method `can_create_post` that checks if a user has enough points to create a post. 

Assume the existence of a `User` model with a `points` field. The `earn_points` and `use_points` methods should modify the `points` field accordingly. The `can_create_post` method should return a boolean indicating whether the user has enough points to create a post.
"""

def can_create_post(user, required_points):
    """
    Checks if a user has enough points to create a post.

    Args:
        user (User): The user to check.
        required_points (int): The number of points required to create a post.

    Returns:
        bool: True if the user has enough points, False otherwise.
    """
    return user.points >= required_points