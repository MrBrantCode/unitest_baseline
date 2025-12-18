"""
QUESTION:
Design a function named `find_longest_word` that takes an array of strings as input and returns the longest word found in the array. The input strings can contain special characters and whitespace. If multiple words have the same maximum length, return the word that appears first in the array. Do not use any built-in functions or libraries to find the longest word. The function should achieve a time complexity of O(n), where n is the total number of characters in all the strings combined.
"""

def find_longest_word(strings):
    max_length = 0
    longest_word = ""

    for string in strings:
        current_word = ""
        current_length = 0

        for char in string:
            if char.isalpha():
                current_word += char
                current_length += 1
            else:
                if current_length > max_length:
                    max_length = current_length
                    longest_word = current_word
                current_word = ""
                current_length = 0

        if current_length > max_length:
            max_length = current_length
            longest_word = current_word

    return longest_word