"""
QUESTION:
Write a function named most_frequent_character that takes a string as input, counts the frequency of each alphabetic character in the string while ignoring case sensitivity and spaces, and returns the character with the highest frequency. If multiple characters have the same highest frequency, return the one that appears first in the string.
"""

def most_frequent_character(string):
    string = string.lower()
    char_count = {}
    for char in string:
        if char != ' ':
            char_count[char] = char_count.get(char, 0) + 1
    max_freq = max(char_count.values())
    most_frequent = [char for char, freq in char_count.items() if freq == max_freq]
    return most_frequent[0]