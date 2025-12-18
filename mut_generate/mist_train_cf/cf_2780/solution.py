"""
QUESTION:
Create a function called `format_sentence` that takes a string sentence as an argument. The function should capitalize the first letter of each word in the sentence, handling cases where words start with numbers or special characters, and preserving capitalization of already capitalized words. It should also handle sentences that contain special characters within words, numbers as separate words, and punctuation marks at the end of sentences. The function should be case-insensitive and assume the input sentence is not empty.
"""

import re

def format_sentence(sentence):
    words = re.findall(r'\w+|[^\w\s]', sentence)
    formatted_words = []
    for word in words:
        if word.isalpha():
            formatted_word = word.capitalize()
        else:
            formatted_word = word[0].capitalize() + word[1:]
        formatted_words.append(formatted_word)
    formatted_sentence = ' '.join(formatted_words)
    return formatted_sentence