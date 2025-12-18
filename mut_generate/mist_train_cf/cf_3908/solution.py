"""
QUESTION:
Implement a function called `is_palindrome(string)` that checks if a given string is a palindrome, considering case sensitivity, spaces, and special characters. The function should ignore spaces and special characters when determining if a string is a palindrome. The algorithm should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1), i.e., constant space usage. The function should return a boolean value indicating whether the string is a palindrome.
"""

def is_palindrome(s):
    """
    Checks if a given string is a palindrome, considering case sensitivity, 
    spaces, and special characters. The function ignores spaces and special 
    characters when determining if a string is a palindrome.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """

    # Convert the string to lowercase to consider case sensitivity
    s = s.lower()
    
    # Initialize two pointers, one at the start and one at the end of the string
    start = 0
    end = len(s) - 1

    # Iterate through the string from both ends towards the middle
    while start < end:
        # If the character at the start is not alphanumeric, move the start pointer forward
        if not s[start].isalnum():
            start += 1
        # If the character at the end is not alphanumeric, move the end pointer backward
        elif not s[end].isalnum():
            end -= 1
        # If the characters at the start and end are not equal, the string is not a palindrome
        elif s[start] != s[end]:
            return False
        # Move both pointers towards the middle
        else:
            start += 1
            end -= 1

    # If the loop completes without finding any unequal characters, the string is a palindrome
    return True