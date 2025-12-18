"""
QUESTION:
Replace all occurrences of a word with its synonyms in a given sentence. The function should take a sentence and a dictionary of word synonyms as input, and return the modified sentence with all occurrences of the words in the dictionary replaced with their synonyms. The function should be case-sensitive and should not modify words that are part of other words.
"""

import re

def replace_with_synonyms(sentence, synonyms):
    pattern = re.compile(r'\b(' + '|'.join(synonyms.keys()) + r')\b')
    modified_sentence = pattern.sub(lambda x: synonyms[x.group()], sentence)
    return modified_sentence