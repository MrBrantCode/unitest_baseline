"""
QUESTION:
Write a function named `compare_strings` that takes two strings, `string1` and `string2`, as input. The function should compare these strings character by character and return the number of matching characters. A character is considered matching if it is the same in both strings and matches the regular expression /^[a-z]+$/. The function should assume that the lengths of `string1` and `string2` are equal; if they are not, it should return an error message.
"""

import re

def compare_strings(string1, string2):
    # Step 1: Check if the lengths of string1 and string2 are equal
    if len(string1) != len(string2):
        return "Error: Strings should be of equal length"

    # Step 2: Iterate through each character in string1 and string2
    count = 0
    for char1, char2 in zip(string1, string2):
        # Step 3: Compare each character in string1 with the corresponding character in string2
        if char1 == char2 and re.match("^[a-z]+$", char1):
            # Step 4: If the characters match the regular expression, increment the count
            count += 1
    
    # Step 7: Return the final count of matching characters
    return count