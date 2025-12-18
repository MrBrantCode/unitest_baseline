"""
QUESTION:
Write a function `find_string_length` that calculates the length of a given null-terminated string without using built-in functions or libraries that directly give the length of a string. The function should return the length of the string and have a time complexity of less than or equal to O(n), where n is the length of the string. Note that the string is assumed to end with a null character '\0'.
"""

def find_string_length(string):
    length = 0
    index = 0
    
    while string[index] != '\0':
        length += 1
        index += 1
    
    return length