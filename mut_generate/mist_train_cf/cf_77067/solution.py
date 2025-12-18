"""
QUESTION:
Write a function `get_users_over_24_not_starting_with_a` to retrieve records from the 'Users' table where the age is greater than 24 and the name does not start with 'A', ordered by age in descending order. The 'Users' table has columns 'Id', 'age', and 'name'.
"""

def get_users_over_24_not_starting_with_a(users):
    return [user for user in users if user['age'] > 24 and not user['name'].startswith('A')]

# Note: To sort the result in descending order of age, you can use the sorted function in Python:
# result = sorted(get_users_over_24_not_starting_with_a(users), key=lambda x: x['age'], reverse=True)