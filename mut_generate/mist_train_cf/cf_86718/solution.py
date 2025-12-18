"""
QUESTION:
Write a function named `reverse_string` that takes a string as input and returns its reverse. The function should not use any built-in string reversal functions or methods. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def reverse_string(string):
    length = len(string)
    reversed_string = ""
    for i in range(length-1, -1, -1):
        reversed_string += string[i]
    return reversed_string