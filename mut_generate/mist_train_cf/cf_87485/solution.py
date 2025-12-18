"""
QUESTION:
Write a function called `reverse_string` that takes a string as input and returns the reversed string without using any built-in functions or libraries, using only basic data structures like strings, lists, and loops, and achieving a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(s):
    reversed_str = ""
    for i in range(len(s)-1, -1, -1):
        reversed_str += s[i]
    return reversed_str