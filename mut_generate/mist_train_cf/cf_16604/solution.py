"""
QUESTION:
Write a function `find_third_o` that takes a string as input and returns the 1-indexed position of the 3rd occurrence of the letter 'o' in the string. If the string does not contain three 'o's, return -1. You cannot use any string manipulation functions or methods.
"""

def find_third_o(string):
    count = 0
    for index, char in enumerate(string):
        if char == 'o':
            count += 1
            if count == 3:
                return index + 1  
    return -1 