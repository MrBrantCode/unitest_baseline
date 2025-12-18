"""
QUESTION:
Write a function `update_users` that takes a list of user objects as input. Each user object is a dictionary containing the keys "name" and "age". The function should increment the "age" value of each user by 5 if their name starts with a vowel and their age is less than 40. The function should remove any user whose name contains a special character or a number. The function should return the updated list of users sorted in descending order based on the "age" value.
"""

def update_users(users):
    """
    Updates a list of user objects by incrementing the "age" value of each user by 5 if their name starts with a vowel and their age is less than 40.
    Removes any user whose name contains a special character or a number.
    Returns the updated list of users sorted in descending order based on the "age" value.

    Args:
        users (list): A list of user objects, where each user object is a dictionary containing the keys "name" and "age".

    Returns:
        list: The updated list of users.
    """

    # Function to check if a character is a vowel
    def is_vowel(char):
        return char.lower() in ['a', 'e', 'i', 'o', 'u']

    # Update age and remove invalid users
    updated_users = []
    for user in users:
        name = user['name']
        age = user['age']
        first_char = name[0]
        if is_vowel(first_char) and age < 40 and name.isalpha():
            user['age'] = age + 5
            updated_users.append(user)

    # Sort updated array in descending order based on age
    updated_users.sort(key=lambda x: x['age'], reverse=True)

    return updated_users