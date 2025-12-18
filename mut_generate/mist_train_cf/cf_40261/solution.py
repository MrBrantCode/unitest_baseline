"""
QUESTION:
Implement a function `find_palindromes` that takes a list of strings as input and returns a new list containing only the strings that are palindromes, ignoring spaces, punctuation, and capitalization. The function should return the original strings that are palindromes, not the cleaned versions.
"""

def find_palindromes(strings):
    """
    Returns a list of palindromes from the input list of strings.

    Args:
    strings: A list of strings.

    Returns:
    A list of strings that are palindromes.
    """
    palindromes = []
    for string in strings:
        # Remove spaces and convert to lowercase
        clean_string = ''.join(e for e in string if e.isalnum()).lower()
        if clean_string == clean_string[::-1]:  # Check if the string is a palindrome
            palindromes.append(string)
    return palindromes