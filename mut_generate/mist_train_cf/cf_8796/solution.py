"""
QUESTION:
Create a function `find_most_frequent_word` in a class with an initializer that takes a string `text` as input, which returns the word that has the maximum frequency in the string. The function should ignore punctuation marks, special characters, and numbers, and consider only alphabetic characters. It should handle cases with multiple words having the same maximum frequency by returning the word that occurs first in the string. The function should efficiently handle large input strings and various edge cases such as words separated by multiple spaces, quotation marks, hyphens, forward slashes, and periods.
"""

import re

def find_most_frequent_word(text):
    cleaned_text = re.sub(r'[^\w\s/\'".-]', '', text.lower())
    words = re.split(r'\s+|(?<=[\'"])|(?=[\'"])|(?<=[/.-])|(?=[/.-])', cleaned_text)
    words = [word for word in words if len(word) > 1]
    
    frequency_count = {}
    max_frequency = 0
    most_frequent_word = ""

    for word in words:
        if word in frequency_count:
            frequency_count[word] += 1
        else:
            frequency_count[word] = 1

        if frequency_count[word] > max_frequency:
            max_frequency = frequency_count[word]
            most_frequent_word = word

    return most_frequent_word