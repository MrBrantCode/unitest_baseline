"""
QUESTION:
Implement a function named `count_character` that takes a string and a character as input and returns the number of occurrences of the character in the string. The function must have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1). The solution must not use any built-in functions or methods that directly count the occurrences of the character in the string.
"""

def count_character(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count