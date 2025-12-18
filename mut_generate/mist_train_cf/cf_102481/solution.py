"""
QUESTION:
Create a function `distinct_names_by_age` to retrieve distinct first names of users from a database. The users should be between 18 and 30 years old, and the names should be sorted in alphabetical order. The database contains user documents with fields `firstName`, `lastName`, `email`, and `age`.
"""

def distinct_names_by_age(users):
    return sorted(set(user['firstName'] for user in users if 18 <= user['age'] <= 30))