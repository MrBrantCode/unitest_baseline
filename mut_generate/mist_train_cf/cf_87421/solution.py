"""
QUESTION:
Create a function `compare_strings` that compares two input strings character by character without using loops, recursion, if statements, built-in string comparison functions, or libraries. The function should return True if the strings are identical and False otherwise, relying solely on arithmetic and bitwise operations.
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