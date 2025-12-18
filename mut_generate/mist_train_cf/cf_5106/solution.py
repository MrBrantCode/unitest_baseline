"""
QUESTION:
Create a function `check_order_with_spaces` that takes two strings as input, `string1` and `string2`, and returns a boolean indicating whether the characters in `string1` appear in the same order in `string2`, with at least two spaces between each character in `string2`. The function should have a time complexity of O(n+m), where n and m are the lengths of `string1` and `string2` respectively.
"""

def check_order_with_spaces(string1, string2):
    # Remove all spaces from string2
    string2 = string2.replace(" ", "")

    # Initialize pointers for both strings
    i = 0
    j = 0

    # Loop until we reach the end of both strings
    while i < len(string1) and j < len(string2):
        # Check if the characters at the current positions match
        if string1[i] == string2[j]:
            # Move the pointer in string1
            i += 1
        # Move the pointer in string2
        j += 1

    # Check if we reached the end of string1
    if i == len(string1):
        return True
    else:
        return False