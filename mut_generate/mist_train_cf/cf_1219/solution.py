"""
QUESTION:
Write a function `convert_string_to_word_list` that takes a string as input, converts it to a list of words (separated by spaces), and returns the list of words in reverse alphabetical order. The function should exclude punctuation marks, special characters, and numbers from the output list. If two words have the same reverse alphabetical order, their original order in the string should be reversed. The function should have a time complexity of O(n*log(n)) or better and a space complexity of O(n), where n is the length of the string. The function should handle strings with leading and trailing whitespace characters, multiple consecutive whitespace characters, multiple consecutive punctuation marks or special characters, non-ASCII characters, and mixed uppercase and lowercase characters.
"""

import re

def convert_string_to_word_list(string):
    string = string.strip()
    words = re.findall(r"[\w']+|[.,!?;]", string)
    words = [word for word in words if word.isalpha()]
    words.sort(reverse=True)
    words = sorted(words, key=lambda x: (x[::-1], words.index(x)))
    return words