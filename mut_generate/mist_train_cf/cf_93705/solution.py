"""
QUESTION:
Write a function `are_strings_equal` that takes two strings `string1` and `string2` as input and returns `True` if they are equal and `False` otherwise. The comparison should be case-sensitive, consider whitespace, and ignore punctuation marks. The function should not use any built-in string comparison functions or methods.
"""

def are_strings_equal(string1, string2):
    # Remove punctuation marks from both strings
    modified_string1 = ''.join(c for c in string1 if c.isalnum() or c.isspace())
    modified_string2 = ''.join(c for c in string2 if c.isalnum() or c.isspace())

    # Compare the length of modified strings
    if len(modified_string1) != len(modified_string2):
        return False

    # Compare characters of modified strings
    for i in range(len(modified_string1)):
        if modified_string1[i] != modified_string2[i]:
            return False

    # Strings are equal
    return True