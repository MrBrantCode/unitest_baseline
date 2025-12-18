"""
QUESTION:
Write a function named `longest_word_length` that takes a string as input and returns the length of the longest word that can be formed by rearranging the characters of the string. The function should not take any other parameters and should only consider the characters in the input string to determine the length of the longest word.
"""

from collections import Counter

def longest_word_length(s):
    char_count = Counter(s.replace(" ", ""))
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    longest_word = ''.join([k * v for k, v in sorted_chars])
    return len(longest_word)