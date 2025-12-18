"""
QUESTION:
Write a function called `format_string` that takes a string as input and returns a string where every word starts with a capital letter and the rest of the word is in lowercase, with no leading or trailing spaces and no multiple spaces between words. Assume the input string contains only alphabetical characters and spaces.
"""

def format_string(string):
    # Remove leading and trailing spaces
    string = string.strip()

    # Split the string into words
    words = string.split()

    # Capitalize the first letter of each word and make the rest lowercase
    words = [word.capitalize() for word in words]

    # Join the words into a single string with a space between each word
    formatted_string = " ".join(words)

    return formatted_string