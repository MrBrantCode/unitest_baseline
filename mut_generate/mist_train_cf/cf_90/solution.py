"""
QUESTION:
Create a function `character_frequency` that takes a string as input and returns a dictionary containing the frequency of each unique character, ignoring case sensitivity and whitespace characters. The function should have a space complexity of O(n), where n is the length of the string.
"""

def character_frequency(s):
    frequencies = {}
    s = s.replace(" ", "").lower()
    for char in s:
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies