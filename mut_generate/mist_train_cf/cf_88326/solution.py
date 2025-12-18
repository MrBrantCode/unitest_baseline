"""
QUESTION:
Create a function called `reverse_string` that takes a string `s` as input and returns its reversal. The function must not use any built-in string manipulation functions or methods and must not use any built-in data structures like lists or arrays. The time complexity should be O(n) and the space complexity should be O(1), where `n` is the length of the string `s`.
"""

def reverse_string(s):
    reversed_str = ""
    for i in range(len(s)-1, -1, -1):
        reversed_str += s[i]
    return reversed_str