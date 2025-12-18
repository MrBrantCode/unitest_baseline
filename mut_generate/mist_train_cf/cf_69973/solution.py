"""
QUESTION:
Write a function named `append_string` that takes two parameters: a paragraph of text and a string to append. The function should append the given string to the end of every unique word in the paragraph and return the modified paragraph.
"""

import re

def append_string(paragraph, string_to_append):
    # Tokenize the paragraph into words
    words = re.findall(r'\b\w+\b', paragraph)

    # Map each unique word to itself plus the string to append
    transformed_words = {word: word + string_to_append for word in set(words)}

    # Replace the words in the original paragraph
    transformed_paragraph = re.sub(r'\b\w+\b', lambda match: transformed_words[match.group(0)], paragraph)

    return transformed_paragraph