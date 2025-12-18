"""
QUESTION:
Write a function named `reversed_word_except_list` that accepts two parameters: `text` (a string containing a paragraph) and `except_list` (a list of words to exclude from reversal). The function should reverse each word in the paragraph individually while maintaining their original order, excluding the words specified in `except_list`. The function should also preserve any punctuation found in the string, ensuring they stay attached to their relevant word, and retain the spacing exactly as it was in the original input.
"""

import re

def reversed_word_except_list(text, except_list=[]):
    def reverse_word(word): 
        punc = '' 
        while len(word) > 0 and not word[-1].isalpha(): 
            punc = word[-1] + punc 
            word = word[:-1]
        return word[::-1] + punc

    words = re.findall(r'\b\w+\b', text) 
    result = text
    for word in words:
        if word not in except_list:
            result = result.replace(word, reverse_word(word))
    return result