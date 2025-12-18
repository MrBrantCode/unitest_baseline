"""
QUESTION:
Write a function `reverse_unique_words` that takes a string as input, reverses the order of its unique words, and ignores any punctuation marks. The function should return a list of words in reverse order.
"""

import re
from collections import OrderedDict

def reverse_unique_words(s):
    words = re.sub('[^a-zA-Z0-9\s]', '', s).split()
    unique_words = list(OrderedDict.fromkeys(words))
    return unique_words[::-1]