"""
QUESTION:
Implement the function `advanced_happy_string(s)` that takes a string `s` as input and returns `True` if the string meets the following conditions:

- The same three-letter combination should not appear more than once throughout the string.
- The third character in each consecutive three-letter combination must be different from the first character in the next three-letter combination.

Use dictionaries and sets to solve the problem, tracking character counts and unique three-letter combinations respectively. The function should return `False` if the string length is less than 3.
"""

def advanced_happy_string(s):
    if len(s) < 3:
        return False

    # Build the list of 3-character substrings
    substrings = [s[i:i+3] for i in range(len(s)-2)]

    # Store each three-character substring and check condition
    subsets = set()
    for i in range(len(substrings)):
        if substrings[i] in subsets:
            return False # The same three-letter combination appears more than once

        if i < len(substrings)-1 and substrings[i][2] == substrings[i+1][0]:
            return False # Third character equal to the first character of next substring

        subsets.add(substrings[i])

    return True