"""
QUESTION:
Implement a function `is_palindrome(string: str) -> bool` that checks if a given string can be converted to a palindrome, considering only alphanumeric characters and ignoring the case. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string. The implementation should not use any additional data structures or global variables.
"""

def is_palindrome(string: str) -> bool:
    """
    Checks if a given string can be converted to a palindrome, considering only alphanumeric characters and ignoring the case.

    Args:
        string (str): The input string to check.

    Returns:
        bool: True if the string can be converted to a palindrome, False otherwise.
    """
    left, right = 0, len(string) - 1

    while left < right:
        if not (string[left].isalpha() or string[left].isdigit()):
            left += 1
        elif not (string[right].isalpha() or string[right].isdigit()):
            right -= 1
        elif string[left].lower() != string[right].lower():
            return False
        else:
            left += 1
            right -= 1

    return True