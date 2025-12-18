"""
QUESTION:
Write a function `not_reverse_binary(a: str) -> str` that takes a string `a` consisting only of '1's and '0's, reverses the string, and performs a bit-wise NOT operation on the reversed string, returning the result as a string.
"""

def not_reverse_binary(a: str) -> str:
    result = ""
    for i in range(len(a) - 1, -1, -1):  # Iterating through "a" in reverse order
        result += str(int(not int(a[i])))  # Performing bitwise NOT and adding to result
    return result