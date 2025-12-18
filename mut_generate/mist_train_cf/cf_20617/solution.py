"""
QUESTION:
Write a function `sort_letters(string)` that takes a string as input and returns a new string containing unique lowercase letters from the input string, sorted in ascending order of their ASCII values, while ignoring any non-lowercase characters.
"""

def sort_letters(string):
    # Create an empty list to store the lowercase letters
    letters = []

    # Iterate over each character in the string
    for char in string:
        # Check if the character is a lowercase letter
        if char.islower():
            # Add the lowercase letter to the list
            letters.append(char)

    # Remove duplicate letters from the list
    letters = list(set(letters))

    # Sort the letters based on their ASCII values in ascending order
    sorted_letters = sorted(letters, key=lambda x: ord(x))

    # Create a new string with the sorted letters
    new_string = ''.join(sorted_letters)

    # Return the new string
    return new_string