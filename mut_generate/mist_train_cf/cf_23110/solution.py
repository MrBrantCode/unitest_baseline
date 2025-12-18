"""
QUESTION:
Write a function `is_palindrome(string)` to determine whether the given string is a palindrome or not. The input string can contain any printable ASCII characters and its length can be up to 10^6 characters. The function should return `True` for palindrome strings and `False` for non-palindrome strings.
"""

def is_palindrome(string):
    # Convert the input string to lowercase
    string = string.lower()

    # Remove non-alphanumeric characters from the string
    string = ''.join(char for char in string if char.isalnum())

    # Initialize pointers
    start = 0
    end = len(string) - 1

    # Traverse the string from both ends
    while start < end:
        # Compare characters at the pointers
        if string[start] != string[end]:
            return False
        # Move pointers towards the center
        start += 1
        end -= 1

    # Return True if pointers meet or cross each other
    return True