"""
QUESTION:
Write a function named `is_spam` that takes a string `text` as input and returns `True` if the text is classified as spam and `False` otherwise. The function should be able to detect potential spam by analyzing both the content and writing style, taking into consideration that certain words, phrases, and punctuation might be altered to avoid detection. The function should be case-insensitive and should handle typical spam word modifications such as '@' to 'a', '!' to 'i', '0' to 'o', '3' to 'e', '€' to 'e', and '1' to 'i'. The function should use a predefined list of spam words.
"""

import re

def is_spam(text):
    # create a dictionary to decode alternations
    decoder = {'@': 'a', '!': 'i', '0': 'o', '3': 'e', '€': 'e', '1': 'i'}
    # create a spam_words list
    spam_words = ['spam', 'winning', 'free', 'congratulations']
    
    # process words in spam_words
    for word in spam_words:
        pattern = ''.join(decoder.get(c, c) for c in word)
        # if the spam word (decoded) is found in the text, return True
        if re.findall(pattern, text, re.IGNORECASE):
            return True

    return False