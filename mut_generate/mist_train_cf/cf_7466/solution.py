"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of strings as input, removes duplicates while ignoring case sensitivity, removes leading/trailing whitespaces, and removes palindromes. The function should return a list of unique strings.
"""

def remove_duplicates(strings):
    unique_strings = []
    for string in strings:
        # Remove leading and trailing whitespace
        string = string.strip()
        # Convert string to lowercase for case-insensitive comparison
        string = string.lower()
        # Check if string is a palindrome
        if string == string[::-1]:
            continue
        # Check if string is already in unique_strings
        if string in unique_strings:
            continue
        # Add string to unique_strings
        unique_strings.append(string)
    return unique_strings