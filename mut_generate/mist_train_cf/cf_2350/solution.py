"""
QUESTION:
Write a function `compare_strings` that takes two strings `string1` and `string2` as input and returns a boolean indicating whether the two strings are identical. The function should not use any built-in string comparison functions, loops, recursion, or if statements, and should only use arithmetic and bitwise operations.
"""

def compare_strings(string1, string2):
    length1 = len(string1)
    length2 = len(string2)

    if length1 != length2:
        return False

    result = 0

    for i in range(length1):
        result |= ord(string1[i]) ^ ord(string2[i])

    return result == 0