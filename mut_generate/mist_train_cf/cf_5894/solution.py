"""
QUESTION:
Create a function named `is_palindrome` that takes a string as input. The function should determine whether the input string is a palindrome, ignoring special characters, whitespace, numbers, and punctuation marks, and considering the comparison to be case-insensitive. The function should have a time complexity of O(n), where n is the length of the input string, and be able to handle strings of length up to 10^6 characters efficiently without exceeding memory limitations.
"""

def is_palindrome(string):
    """
    Determine whether the input string is a palindrome, ignoring special characters, 
    whitespace, numbers, and punctuation marks, and considering the comparison to be case-insensitive.

    Args:
        string (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Time complexity: O(n), where n is the length of the input string.
    """
    
    # Remove special characters, whitespace, numbers, and punctuation marks
    string = ''.join(e for e in string if e.isalnum())
    
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()
    
    # Check if the string is a palindrome
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True