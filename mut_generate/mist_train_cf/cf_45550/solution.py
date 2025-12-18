"""
QUESTION:
Implement the function `is_happy(s)` to check if a given string `s` meets the following conditions:

- The string must be at least 3 characters long.
- Every unique character in the string appears at least twice, but no more than four times.
- Each consecutive set of 3 characters is distinct.
- No character appears three times in a row.
- No character appears both at the beginning and the end of the string.

Return `True` if the string meets all conditions, and `False` otherwise.
"""

def is_happy(s):
    # Checking the first condition - string must be at least 3 characters long
    if len(s) < 3:
        return False

    # Third condition - every unique character appears at least twice, but not more than four times
    char_count = {char: s.count(char) for char in set(s)}
    for count in char_count.values():
        if count < 2 or count > 4:
            return False

    # Checking the second condition - each consecutive set of 3 characters are distinct
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) != 3:
            return False

    # Checking the fourth condition - no character appears thrice in consecutive sequence
    for i in range(len(s) - 2):
        if s[i] == s[i+1] == s[i+2]:
            return False

    # Integrating the new condition - no character to be allowed to occur both at the beginning and the end of the string
    if s[0] == s[-1]:
        return False

    # If it passes all conditions
    return True