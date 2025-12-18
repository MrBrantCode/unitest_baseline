"""
QUESTION:
Create a function named `generate_usernames` that takes two lists of strings, `first_names` and `last_names`, as input and returns a list of unique usernames. The function should combine each corresponding first and last name, convert them to lowercase, and separate them with an underscore. If a username is already taken, the function should append a number to the username to make it unique. The function should return a list of all unique usernames. The function should handle any number of input names.
"""

def generate_usernames(first_names, last_names):
    usernames = []
    name_count = {}
    
    for first, last in zip(first_names, last_names):
        username = f"{first.lower()}_{last.lower()}"
        if username in name_count:
            name_count[username] += 1
            username = f"{username}{name_count[username]}"
        else:
            name_count[username] = 1
        usernames.append(username)
    
    return usernames