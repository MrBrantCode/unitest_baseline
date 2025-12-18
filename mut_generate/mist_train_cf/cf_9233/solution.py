"""
QUESTION:
Implement a function named `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome and `False` otherwise, without using any built-in string manipulation functions or data structures. The input string only contains alphanumeric characters and the comparison is case-sensitive. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def entrance(string):
    start = 0
    end = len(string) - 1
    
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    
    return True