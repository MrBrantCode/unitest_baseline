"""
QUESTION:
Implement a function named `remove_common_characters` that takes two strings `s` and `t` as input and returns two new strings with all common characters removed. The function should ignore the order of characters and consider upper and lower case as the same. Do not use any built-in functions that remove or replace characters in strings.
"""

def remove_common_characters(s, t):
    # Convert both strings to lower case for case-insensitive comparison
    s = s.lower()
    t = t.lower()

    # Create a set of unique common characters
    common = set(s) & set(t)

    # Initialize two new strings to store the result
    new_s = ''
    new_t = ''

    # Iterate over each character in the original strings
    for char in s:
        if char not in common:
            new_s += char

    for char in t:
        if char not in common:
            new_t += char

    # Return the new strings with common characters removed
    return new_s, new_t