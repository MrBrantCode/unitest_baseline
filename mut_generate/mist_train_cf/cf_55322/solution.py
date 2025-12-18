"""
QUESTION:
Implement the `is_happy(s)` function to check if a given string `s` is happy or not. A string is happy if its length is at least 3, every 3 consecutive letters are distinct, every distinct letter appears at least twice, and there should not be any consecutive repeating letters. You must use a dictionary in your solution to store the frequency of distinct letters, and avoid using any string manipulation functions. The function should return `True` if the string is happy, and `False` otherwise.
"""

def is_happy(s):
    """
    Checks if a given string is happy or not.
    
    A string is happy if its length is at least 3, every 3 consecutive letters are distinct, 
    every distinct letter appears at least twice, and there should not be any consecutive repeating letters.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is happy, False otherwise.
    """

    if len(s) < 3:
        return False

    # Use a dictionary to store the frequency of distinct letters.
    letter_count = {}

    # Check for no consecutive repeating letters and update the dictionary.
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
        if s[i] not in letter_count:
            letter_count[s[i]] = 1
        else:
            letter_count[s[i]] += 1

    # Add the last letter to the dictionary.
    if s[-1] not in letter_count:
        letter_count[s[-1]] = 1
    else:
        letter_count[s[-1]] += 1

    # Check if every distinct letter appears at least twice.
    for count in letter_count.values():
        if count < 2:
            return False

    # Check if every 3 consecutive letters are distinct.
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False

    return True