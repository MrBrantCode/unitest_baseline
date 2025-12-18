"""
QUESTION:
Create a function called `generate_unique_id` that takes a string as input and returns a unique ID by performing the following operations: converting to lowercase, removing leading/trailing spaces, replacing consecutive spaces with a single space, removing non-alphanumeric characters, replacing spaces with underscores, handling empty strings, handling strings that start with numbers, and truncating to 20 characters. The function should return "no_id" if the resulting string is empty.
"""

def generate_unique_id(string):
    # Step 1: Convert the string to lowercase
    string = string.lower()

    # Step 2: Remove leading and trailing spaces
    string = string.strip()

    # Step 3: Replace consecutive spaces with a single space
    string = ' '.join(string.split())

    # Step 4: Remove all non-alphanumeric characters
    string = ''.join(c for c in string if c.isalnum() or c.isspace())

    # Step 5: Replace spaces with underscores
    string = string.replace(' ', '_')

    # Step 6: Check if the resulting string is empty
    if not string:
        return 'no_id'

    # Step 7: Check if the resulting string starts with a number
    if string[0].isdigit():
        string = '_' + string

    # Step 8: Truncate the string to the first 20 characters
    if len(string) > 20:
        string = string[:20]

    # Step 9: Return the resulting string as the unique ID
    return string