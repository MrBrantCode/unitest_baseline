"""
QUESTION:
Write a Python function named `replace_word` that takes three parameters: `sentence`, `word`, and `replacement`. The function should replace all occurrences of the specified `word` in the `sentence` with the `replacement`, but only if the `word` is surrounded by spaces. The function should be case-sensitive, and it should handle edge cases where the word appears multiple times, at the beginning or end of the string, or with different capitalizations. The function should not replace the word if it is part of a larger word or surrounded by punctuation marks or other characters.
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