"""
QUESTION:
Create a Python function `count_users` that takes a list of user objects, where each user object is a tuple containing a username and password, and returns a dictionary where the keys are unique usernames and the values are the count of users with that username.
"""

def count_users(user_list):
    user_count = {}
    for user in user_list:
        username = user[0]
        if username in user_count:
            user_count[username] += 1
        else:
            user_count[username] = 1
    return user_count