"""
QUESTION:
Write a function `most_frequent_char` that takes a string as input, ignores any duplicate characters that occur consecutively, and returns the most frequently used character in the string. The function should have a time complexity of O(n), where n is the length of the string.
"""

def most_frequent_char(string):
    # Remove consecutive duplicate characters
    cleaned_string = ""
    prev_char = None
    for char in string:
        if char != prev_char:
            cleaned_string += char
        prev_char = char

    # Count the occurrences of each character
    char_count = {}
    for char in cleaned_string:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the most frequent character
    most_frequent_char = None
    max_count = 0
    for char, count in char_count.items():
        if count > max_count:
            most_frequent_char = char
            max_count = count

    return most_frequent_char