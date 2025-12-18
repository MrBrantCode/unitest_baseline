"""
QUESTION:
Write a function called `reverse_string` that takes a string as input and returns its reversed version. The function must not use any built-in string reversal functions or methods. The time complexity of the solution should be O(n), where n is the length of the input string.
"""

def reverse_string(string):
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string