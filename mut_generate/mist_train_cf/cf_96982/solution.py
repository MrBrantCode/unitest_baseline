"""
QUESTION:
Write a function `is_substring_present(strings, substring)` that checks if the substring is present in any string in the set of strings, where the substring is a palindrome and has a length of 5 or more. The function should return `True` if the substring is found and `False` otherwise.
"""

def is_substring_present(strings, substring):
    """
    Checks if the substring is present in any string in the set of strings.
    The substring is a palindrome and has a length of 5 or more.

    Args:
        strings (list): A list of strings to search in.
        substring (str): The substring to search for.

    Returns:
        bool: True if the substring is found, False otherwise.
    """
    def is_palindrome(string):
        return string == string[::-1]

    for string in strings:
        for i in range(len(string)-4):  # minimum length of substring should be 5
            sub = string[i:i+5]
            if is_palindrome(sub) and substring in sub:
                return True
    return False