"""
QUESTION:
Create a function `sort_users` that sorts a list of user objects in alphabetical order by their 'name' and then by their 'age' in descending order. Each user object is a dictionary containing 'name' (a string), 'age' (an integer), and 'country' (a string). The function should have a time complexity not exceeding O(n log n) and a space complexity not exceeding O(n).
"""

def sort_users(users):
    """
    Sorts a list of user objects in alphabetical order by their 'name' and then by their 'age' in descending order.

    Args:
        users (list): A list of user objects. Each user object is a dictionary containing 'name' (a string), 'age' (an integer), and 'country' (a string).

    Returns:
        list: The sorted list of user objects.
    """
    users.sort(key=lambda user: (user['name'], -user['age']))
    return users