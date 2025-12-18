"""
QUESTION:
Create a function `remove_duplicates` that takes a string as input and returns a new string where all duplicate words are removed, while maintaining the original order of words. The input string contains only spaces as word separators and does not contain punctuation.
"""

def remove_duplicates(my_string):
    my_words = my_string.split(' ')
    my_words = list(dict.fromkeys(my_words))
    return " ".join(my_words)