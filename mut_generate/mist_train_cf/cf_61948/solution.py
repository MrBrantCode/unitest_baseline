"""
QUESTION:
Create a function `count_words_and_check_palindrome` that takes a string of alphanumeric characters and special characters as input. The function should return a dictionary with each unique word in the string as keys, and their corresponding values as another dictionary containing the word count and whether the word is a palindrome or not. The function should ignore case sensitivity and punctuation.
"""

import re
from collections import Counter

def count_words_and_check_palindrome(string_seq):
    res_dict = {}
    string_seq = re.sub(r'\W+', ' ', string_seq).lower()
    word_count = Counter(string_seq.split())
    for word, count in word_count.items():
        is_palindrome = "Yes" if word == word[::-1] else "No"
        res_dict[word] = {"count": count, "palindrome": is_palindrome}
    return res_dict