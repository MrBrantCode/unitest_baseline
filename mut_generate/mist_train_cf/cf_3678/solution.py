"""
QUESTION:
Create a function called `calculate_word_lengths` that takes a string as input and returns a list of integers representing the length of each word in the string. The function should ignore punctuation marks, numbers, and special characters. The list should be sorted in descending order of word lengths. If two words have the same length, they should be sorted in reverse alphabetical order. If two words have the same length and the same reverse alphabetical order, their order of appearance in the original string should be maintained.
"""

def calculate_word_lengths(s):
    cleaned_string = ''.join(c for c in s if c.isalpha() or c.isspace())
    words = cleaned_string.split()
    word_lengths = [len(word) for word in words]
    sorted_word_lengths = sorted(word_lengths, key=lambda x: (-x, words[word_lengths.index(x)][::-1]))
    return sorted_word_lengths