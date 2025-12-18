"""
QUESTION:
Implement a function `generate_unique_username` that generates a unique username based on a user's first name and last name. The username should be in the format "first_initiallastname", where "first_initial" is the first letter of the first name and "lastname" is the last name, all in lowercase. If the generated username already exists in the list of existing usernames, append a number to the username to make it unique.

The function should take three parameters: the first name, the last name, and a list of existing usernames. It should return the unique username as a string.
"""

from typing import List

def generate_unique_username(first_name: str, last_name: str, existing_usernames: List[str]) -> str:
    first_initial = first_name[0].lower()
    base_username = f"{first_initial}{last_name.lower()}"
    username = base_username
    count = 1
    while username in existing_usernames:
        username = f"{base_username}{count}"
        count += 1
    return username