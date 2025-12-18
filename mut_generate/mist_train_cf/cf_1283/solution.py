"""
QUESTION:
Write a function `find_longest_word` that finds the longest word in a given string, ignoring punctuation marks and accounting for multiple occurrences of the same word. The function should handle cases where the string contains special characters such as emojis or accented characters, and it should have a space complexity of less than O(n), where n is the length of the string. The function should return the longest word.
"""

import re

def find_longest_word(string):
    string_without_punctuation = re.sub(r'[^\w\s]', '', string)
    words = string_without_punctuation.split()
    word_frequency = {}

    longest_word = ''
    longest_word_frequency = 0

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

        if word_frequency[word] > longest_word_frequency or (word_frequency[word] == longest_word_frequency and len(word) > len(longest_word)):
            longest_word = word
            longest_word_frequency = word_frequency[word]

    return longest_word