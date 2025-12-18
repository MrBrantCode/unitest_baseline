"""
QUESTION:
Write a function named `reverse_string` that takes a string `s` as input and returns the string reversed, without using any built-in string reversal functions or methods. The function cannot create any new strings or use any additional data structures. The input string will contain at most 10^5 lowercase English letters.
"""

def reverse_string(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str