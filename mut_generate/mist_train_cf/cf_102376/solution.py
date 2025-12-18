"""
QUESTION:
Create a function named `get_last_n_chars` that takes a string and an integer `n` as input and returns a string with the last `n` characters of the given string. If `n` is greater than the length of the string, return the original string. Implement this function with a time complexity of O(n) and a space complexity of O(n), without using any built-in string manipulation functions or methods such as string slicing or string concatenation.
"""

def get_last_n_chars(string, n):
    length = len(string)
    if n >= length:
        result = ""
        for char in string:
            result += char
        return result
    else:
        result = ""
        for i in range(length - n, length):
            result += string[i]
        return result