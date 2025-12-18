"""
QUESTION:
Create a function `get_frequency_hashmap` that takes a string as input and returns a dictionary where each key is a unique word from the string (ignoring case and punctuation), and its corresponding value is a tuple containing the word's frequency in the string and the total count of alphabetic characters in the word.
"""

from collections import Counter
import re

def get_frequency_hashmap(s):
    s = re.sub(r'[^\w\s]','',s)  
    words = s.lower().split()  
    word_count = Counter(words)  
    for word in word_count:
        char_count = sum(c.isalpha() for c in word)  
        word_count[word] = (word_count[word], char_count)  
    return word_count