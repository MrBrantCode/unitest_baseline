"""
QUESTION:
Implement a function named `countOccurrences` that takes two parameters: a string and a character. Return the number of occurrences of the given character in the string, while maintaining a constant space complexity of O(1).
"""

def countOccurrences(string, character):
    counter = 0
    for char in string:
        if char == character:
            counter += 1
    return counter