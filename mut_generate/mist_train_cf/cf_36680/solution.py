"""
QUESTION:
Implement a Python function named `calculate_character_count_and_average_word_length` that takes a string as input and returns a tuple containing two values. The first value is the count of a specific character 'a' in the string, and the second value is the average length of the words in the string. Words are separated by spaces and may contain punctuation marks. The function should assume that the input string contains only ASCII characters and is not empty.
"""

import string

def calculate_character_count_and_average_word_length(file_content):
    specific_char_count = file_content.count('a')
    words = file_content.split()
    words = [word.strip(string.punctuation) for word in words]
    word_lengths = [len(word) for word in words if word]
    average_word_length = sum(word_lengths) / len(word_lengths)
    return specific_char_count, average_word_length