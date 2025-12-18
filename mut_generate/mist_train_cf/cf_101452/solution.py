"""
QUESTION:
Write a `generate_username` function that takes `first_name` and `last_name` as input, and returns a unique username that is at least six characters long and does not include any numbers or special characters. The function should combine the first and last name, remove any non-alphanumeric characters, and append a number if the length is less than six characters. Additionally, the function should ensure that the generated username is unique among all previously generated usernames.
"""

def generate_username(first_name, last_name):
    # keep track of all usernames that have been generated
    all_usernames = generate_username.all_usernames
    # create username by combining first and last name
    username = first_name.lower() + last_name.lower()
    # remove any non-alphanumeric characters from username
    username = ''.join(e for e in username if e.isalnum())
    # add a number to username if it's shorter than six characters
    if len(username) < 6:
        username += str(len(username))
    # check if username already exists, if so add a number to make it unique
    original_username = username
    n = 1
    while username in all_usernames:
        username = original_username + str(n)
        n += 1
    # add new username to set of all usernames and return it
    all_usernames.add(username)
    return username

# initialize the set of all usernames
generate_username.all_usernames = set()