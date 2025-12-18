"""
QUESTION:
Write a Python function named `replace_word_with_synonym` that replaces all occurrences of a specific word with its synonym in a given sentence. The function should use regular expressions and take two parameters: a dictionary of synonyms where keys are words to be replaced and values are their corresponding synonyms, and a sentence where words will be replaced. The function should return the modified sentence. The function should match whole words only, so "bridge" and "bridges" should not be replaced within "bridged".
"""

import re

def replace_word_with_synonym(synonyms, sentence):
    pattern = re.compile(r'\b(' + '|'.join(synonyms.keys()) + r')\b')
    return pattern.sub(lambda x: synonyms[x.group()], sentence)