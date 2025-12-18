"""
QUESTION:
Create a function named `generate_username` that takes in three parameters: `first_name`, `middle_name`, and `last_name` (where `middle_name` is optional), and a list of `existing_usernames`. The function should generate a unique username that meets the following conditions:

* The username is composed of at least six letters and only comprises alphabet letters.
* The username is not identical to any existing usernames in the database.
* The username is not similar to any existing usernames that differ only in middle or last name.
* The username is generated based on the user's names, taking into account the possibility of a middle name or multiple surnames.

The function should return the generated unique username.
"""

def generate_username(first_name, middle_name=None, last_name=None, existing_usernames=None):
    if existing_usernames is None:
        existing_usernames = []
    if middle_name and last_name:
        names = [first_name, middle_name, last_name]
    else:
        names = [first_name, last_name]
    usernames = set()
    for i in range(len(names)):
        for j in range(i+1, len(names)):
            username = names[i] + names[j]
            if len(username) >= 6 and username.isalpha():
                usernames.add(username.lower())

    # Check for any usernames that differ only in middle or last name
    usernames_to_remove = set()
    for username in usernames:
        for existing_username in existing_usernames:
            existing_names = existing_username.split()
            if len(existing_names) >= 2:
                existing_first_name, existing_last_name = existing_names[0], existing_names[-1]
                if existing_last_name.lower() == last_name.lower() and existing_first_name.lower() != first_name.lower():
                    usernames_to_remove.add(username)

            if len(existing_names) >= 3:
                existing_middle_name = existing_names[1]
                if existing_middle_name.lower() == middle_name.lower() and existing_first_name.lower() == first_name.lower() and existing_last_name.lower() != last_name.lower():
                    usernames_to_remove.add(username)

            if existing_username.lower() == username:
                usernames_to_remove.add(username)

    usernames -= usernames_to_remove

    # Find a unique username
    if usernames:
        return random.choice(list(usernames))
    else:
        return None