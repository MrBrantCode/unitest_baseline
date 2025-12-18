"""
QUESTION:
Implement a function named `sort_users` that takes a list of user objects as input, where each user object is a dictionary containing 'name' and 'age'. The function should return a new list that only includes users with ages between 18 and 60 (inclusive), sorted in descending order by age and then in ascending order by name.
"""

def sort_users(users):
    """
    This function filters a list of user objects to include only users with ages between 18 and 60 (inclusive), 
    and returns the filtered list sorted in descending order by age and then in ascending order by name.

    Args:
        users (list): A list of user objects, where each user object is a dictionary containing 'name' and 'age'.

    Returns:
        list: A new list of user objects filtered and sorted according to the specified criteria.
    """

    # Filter the users with ages between 18 and 60
    filtered_users = [user for user in users if 18 <= user['age'] <= 60]

    # Sort the filtered users by age in descending order and name in ascending order
    sorted_users = sorted(filtered_users, key=lambda user: (-user['age'], user['name']))

    return sorted_users