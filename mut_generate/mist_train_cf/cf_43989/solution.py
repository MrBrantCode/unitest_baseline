"""
QUESTION:
Write a function named `are_rotations` that takes two strings as input and returns `True` if the second string is a rotation of the first string and `False` otherwise. The function should be case sensitive, handle special characters and numbers, and return `False` if the two strings have different lengths.
"""

def are_rotations(string_1, string_2):
    size1 = len(string_1)
    size2 = len(string_2)

    # Check if sizes of two strings are same
    if size1 != size2:
        return False

    # Create a temp string with value str1.str1
    temp = string_1 + string_1

    # Now check if str2 is a substring of temp
    # string.count returns the number of occurrences of the second string in temp
    if (temp.count(string_2)> 0):
        return True
    else:
        return False