"""
QUESTION:
Write a function `replace_word(sentence, word, replacement)` that replaces all occurrences of a specific word in a string with a replacement word, but only if the word is surrounded by spaces. The function should be case-sensitive and should not replace the word if it appears as a substring of another word. The function should also handle edge cases such as multiple consecutive occurrences of the word, different capitalizations, and words surrounded by punctuation marks or other characters.
"""

import re

def replace_word(sentence, word, replacement):
    # Check if either the sentence or word is empty or contains only whitespace characters
    if not sentence.strip() or not word.strip():
        return sentence
    
    # Generate the regular expression pattern to match the word surrounded by spaces
    pattern = r'(?<!\S)' + re.escape(word) + r'(?!\S)'
    
    # Replace all occurrences of the word with the replacement
    replaced_sentence = re.sub(pattern, replacement, sentence)
    
    return replaced_sentence