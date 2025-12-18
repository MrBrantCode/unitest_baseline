"""
QUESTION:
Create a function `first_unique_char` that finds the first unique character in a given string and returns its index position. If no unique character is found, the function should return a dictionary containing all recurring characters with their counts. The function should have a time complexity of O(n).
"""

def first_unique_char(string):
    char_counts = {}
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for index, char in enumerate(string):
        if char_counts[char] == 1:
            return index
    return char_counts