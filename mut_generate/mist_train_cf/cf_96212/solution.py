"""
QUESTION:
Create a function called `sort_letters` that takes a string as input and returns a new string containing only the lowercase letters from the input string in ascending order of their ASCII values, with no duplicates.
"""

def sort_letters(string):
    # Create an empty list to store the lowercase letters
    letters = [char for char in string if char.islower()]

    # Remove duplicate letters from the list
    letters = list(set(letters))

    # Sort the letters based on their ASCII values in ascending order
    sorted_letters = sorted(letters, key=lambda x: ord(x))

    # Create a new string with the sorted letters
    new_string = ''.join(sorted_letters)

    # Return the new string
    return new_string