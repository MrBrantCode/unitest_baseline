"""
QUESTION:
update_json_array(users): Updates the given JSON array of users to increment the "age" value by 5 years if the user's name starts with a vowel and their age is less than 40, and sorts the array in descending order based on the "age" value, excluding users whose names contain special characters or numbers. The function should return the updated JSON array.
"""

import json

def update_json_array(users):
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