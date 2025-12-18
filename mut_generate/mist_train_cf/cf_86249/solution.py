"""
QUESTION:
Create a function `unique_words` that takes a string as input and returns a list of unique alphanumeric words in the order of their appearance. Ignore non-alphanumeric characters and consider 'hello' and 'Hello' as the same word. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(m), where m is the number of unique words in the input string.
"""

import re

def unique_words(string):
    string = re.sub(r'[^\w\s]', '', string).lower()
    unique_words_set = set()
    unique_words_list = []
    for word in string.split():
        if word not in unique_words_set:
            unique_words_set.add(word)
            unique_words_list.append(word)
    return unique_words_list