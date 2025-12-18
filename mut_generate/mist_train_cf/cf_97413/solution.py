"""
QUESTION:
Write a function `check_sequence(arr)` that checks if all the strings in the input sequence `arr` meet the following conditions: 
- All strings in the sequence are unique.
- All strings contain only lowercase alphabets.
- The length of all strings is between 3 and 10 characters (inclusive). 
The function should return `True` if all strings meet the conditions and `False` otherwise.
"""

def check_sequence(arr):
    # Check for uniqueness
    if len(set(arr)) != len(arr):
        return False

    # Check for lowercase alphabets and length between 3 and 10 characters
    for string in arr:
        if not string.islower() or not (3 <= len(string) <= 10):
            return False

    return True