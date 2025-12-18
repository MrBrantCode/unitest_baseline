"""
QUESTION:
Write a function `sort_users` that takes a list of dictionaries representing users with 'last_name', 'first_name', and 'age' keys. The function should return the list sorted in reverse alphabetical order by 'last_name' and in ascending order by 'age' when 'last_name' is identical.
"""

def sort_users(users):
    """
    Sorts a list of users in reverse alphabetical order by 'last_name' 
    and in ascending order by 'age' when 'last_name' is identical.

    Args:
        users (list): A list of dictionaries representing users with 
            'last_name', 'first_name', and 'age' keys.

    Returns:
        list: The sorted list of users.
    """
    # first, sort by age, in ascending order
    users.sort(key=lambda x: x['age'])
    
    # then, sort by last_name, in descending order
    users.sort(key=lambda x: x['last_name'], reverse=True)
    
    return users