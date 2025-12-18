"""
QUESTION:
Implement a function named `count_character(string, char)` that returns the number of occurrences of a given character `char` in a given string `string`. The function should not use any built-in string methods or functions that directly count character occurrences. The time complexity of the solution must be O(n), where n is the length of the string.
"""

def count_character(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count