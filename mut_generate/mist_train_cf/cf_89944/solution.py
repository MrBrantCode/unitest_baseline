"""
QUESTION:
Create a function `remove_duplicates` that takes a list of strings as input and returns a list of strings without duplicates, ignoring case sensitivity. The function should also remove any leading or trailing whitespace from each string before checking for duplicates and exclude any strings that are palindromes.
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