"""
QUESTION:
Write a function `find_most_frequent_character(s)` that takes a string `s` as input and returns the most frequent character in the string without using any built-in functions or libraries. If there are multiple characters with the same highest frequency, the function should return any of them.
"""

def find_most_frequent_character(s):
    char_counts = {}

    for char in s:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    most_frequent_char = None
    highest_count = 0
    for char, count in char_counts.items():
        if count > highest_count:
            most_frequent_char = char
            highest_count = count

    return most_frequent_char