"""
QUESTION:
Write a function called `reverse_string(s)` that takes a string `s` as input and returns the reversed string. The function should not use any built-in string manipulation functions or methods and should not use any built-in data structures such as lists or arrays. The solution should have a time complexity of O(n) and a space complexity of O(1), where `n` is the length of the string `s`.
"""

def reverse_string(s):
    reversed_str = ""
    for i in range(len(s)-1, -1, -1):
        reversed_str += s[i]
    return reversed_str