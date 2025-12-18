"""
QUESTION:
Create a function called `count_characters` that takes a string as input and returns a dictionary where the keys are the alphanumeric characters in the string and the values are the counts of each character. The function should exclude special characters (any character that is not a letter or a digit) and have a time complexity of O(n), where n is the length of the string, and a space complexity of O(k), where k is the number of unique alphanumeric characters in the string.
"""

def count_characters(string):
    char_counts = {}
    for char in string:
        if char.isalnum():
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts