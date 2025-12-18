"""
QUESTION:
Create a function named compare_word_sets that takes two parameters, phrase1 and phrase2, both of type string. The function should compare the two phrases and return True if they contain the same set of words and the same frequency of each word, disregarding case sensitivity, word duplicates, and punctuation marks, and False otherwise.
"""

import collections
import string

def compare_word_sets(phrase1: str, phrase2: str):
    translator = str.maketrans('', '', string.punctuation)
    phrase1_no_punct = phrase1.translate(translator)
    phrase2_no_punct = phrase2.translate(translator)
    
    word_count1 = collections.Counter(phrase1_no_punct.lower().split())
    word_count2 = collections.Counter(phrase2_no_punct.lower().split())
    
    return word_count1 == word_count2