"""
QUESTION:
Create a function `count_unique_characters` that takes a string as input and returns a dictionary with the count of each unique alphabetical character in the string, excluding any whitespace characters and non-alphabetical characters, in a case-insensitive manner.
"""

def count_unique_characters(string):
    string = string.replace(" ", "")
    string = string.lower()
    counts = {}
    for char in string:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts