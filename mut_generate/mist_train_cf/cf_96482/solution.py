"""
QUESTION:
Implement a function `reverse_string` that takes a string as input and returns its reversed version. The function should not use any built-in string reversal functions or methods. The solution must have a time complexity of O(n).
"""

def reverse_string(string):
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string