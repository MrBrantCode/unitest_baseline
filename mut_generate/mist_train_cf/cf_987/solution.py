"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the reverse of the string. The function should not use any built-in string reversal functions or methods. The time complexity of the solution should be O(n) and the space complexity should be O(1).
"""

def reverse_string(s):
    length = len(s)
    reversed_string = ""
    for i in range(length-1, -1, -1):
        reversed_string += s[i]
    return reversed_string