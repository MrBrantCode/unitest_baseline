"""
QUESTION:
Design a function named `reverse_and_remove_duplicates` that takes a string input, removes any non-alphabet characters, reverses the order of its words, and excludes any consecutive duplicate words in the reversed string. The function should achieve this with a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

import re

def reverse_and_remove_duplicates(string):
    cleaned_string = re.sub(r'[^a-zA-Z\s]', '', string)
    words = cleaned_string.split()
    reversed_words = words[::-1]
    result = []
    for i in range(len(reversed_words)):
        if i == 0 or reversed_words[i] != reversed_words[i-1]:
            result.append(reversed_words[i])
    return ' '.join(result)