"""
QUESTION:
Create a function called `count_word_frequencies` that takes a string as input. The function should remove punctuation marks, convert the string to lowercase, remove common stop words, and return a dictionary with the frequency of each word in the string. The function should exclude words such as 'the', 'and', 'is', 'of', 'to', 'in', 'it', 'that', 'you' from the word count.
"""

import re
from collections import Counter

def count_word_frequencies(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    stop_words = ['the', 'and', 'is', 'of', 'to', 'in', 'it', 'that', 'you']
    words = [word for word in words if word not in stop_words]
    return Counter(words)