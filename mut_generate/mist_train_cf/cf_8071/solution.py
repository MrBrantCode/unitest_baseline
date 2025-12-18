"""
QUESTION:
Write a function named `sort_users` that sorts a list of user objects in alphabetical order by their 'name' and then by their 'age' in descending order. Each user object is a dictionary containing 'name' (string), 'age' (integer), and 'country' (string) attributes. The time complexity of the solution should not exceed O(n log n) and the space complexity should not exceed O(n).
"""

def sort_users(users):
    """
    Sorts a list of user objects in alphabetical order by their 'name' and then by their 'age' in descending order.

    Args:
        users (list): A list of user objects, each containing 'name' (string), 'age' (integer), and 'country' (string) attributes.

    Returns:
        list: The sorted list of user objects.
    """
    return sorted(users, key=lambda user: (user['name'], -user['age']))