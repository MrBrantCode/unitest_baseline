"""
QUESTION:
Create a function `check_order` that takes two strings as input, `string1` and `string2`, and checks if the characters in `string1` appear in the same order as in `string2`. The function should have a time complexity of O(n+m), where n and m are the lengths of `string1` and `string2` respectively.
"""

def check_order(string1, string2):
    """
    Checks if the characters in string1 appear in the same order as in string2.

    Args:
        string1 (str): The first string to check.
        string2 (str): The second string to check.

    Returns:
        bool: True if the characters in string1 appear in the same order as in string2, False otherwise.
    """

    # Initialize two pointers for string1 and string2
    pointer1 = 0
    pointer2 = 0
    
    # Iterate through the characters of string1 and string2
    while pointer1 < len(string1) and pointer2 < len(string2):
        # If the characters match, move the pointer for string1
        if string1[pointer1] == string2[pointer2]:
            pointer1 += 1
        # Move the pointer for string2 in any case
        pointer2 += 1
    
    # If all characters in string1 have been found in string2 in the same order, return True
    return pointer1 == len(string1)