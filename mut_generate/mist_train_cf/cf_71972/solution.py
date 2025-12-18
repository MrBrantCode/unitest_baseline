"""
QUESTION:
Transform the string 'sad' into 'happy' using a sequence of single character replacements. Implement a function `lexical_transform(start_word, end_word)` that returns a list of strings representing the sequence of transformations, assuming that the lengths of `start_word` and `end_word` are the same, and each transformation is a valid English word.
"""

import string

def lexical_transform(start_word, end_word):
    temp_word = list(start_word)
    end_word = list(end_word)

    transformations = [start_word]
    alphabet = string.ascii_lowercase

    for char_pos in range(len(temp_word)):
        if temp_word[char_pos] != end_word[char_pos]:
            for alphabet_char in alphabet:
                temp_word[char_pos] = alphabet_char
                if temp_word[char_pos] == end_word[char_pos]:
                    transformations.append(''.join(temp_word))
                    break

    return transformations