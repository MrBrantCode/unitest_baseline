"""
QUESTION:
Implement a function replace_x_with_y that takes a string as input and returns a new string where all occurrences of 'x' are replaced with 'y'. The function should not use any built-in string manipulation functions or regular expressions, have a time complexity of O(n), and use only constant space.
"""

def replace_x_with_y(sentence):
    result = ""
    for ch in sentence:
        if ch == 'x':
            result += 'y'
        else:
            result += ch
    return result