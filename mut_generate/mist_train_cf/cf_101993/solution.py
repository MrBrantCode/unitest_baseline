"""
QUESTION:
Implement a function named `is_palindrome` that takes a string as input and returns a boolean value. The function should return `True` if the input string is the same when read forward and backward (case-insensitive), and `False` otherwise.
"""

def is_palindrome(string):
    # Convert the string to lowercase
    string = string.lower()

    # Initialize two pointers, one at the beginning and one at the end of the string
    start = 0
    end = len(string) - 1

    # Iterate until the pointers meet or cross each other
    while start < end:
        # If the characters at the corresponding positions are not equal, return False
        if string[start] != string[end]:
            return False
        
        # Move the pointers towards each other
        start += 1
        end -= 1

    # If all the characters matched, return True
    return True