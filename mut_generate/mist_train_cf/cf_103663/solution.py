"""
QUESTION:
Write a function `count_occurrences` that takes a string `string` and a character `char` as input and returns the number of occurrences of `char` in `string`. The function should iterate through each character in the string and count the occurrences of the given character.
"""

def count_occurrences(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count