"""
QUESTION:
Write a function `remove_middle_word(sentence)` that takes a string of at least 5 words as input and returns a string where the middle word is removed. The input string will always have an odd number of words, contain only lowercase letters, and not have any punctuation marks or numbers.
"""

def remove_middle_word(sentence):
    words = sentence.split()
    middle_index = len(words) // 2
    words.pop(middle_index)
    new_sentence = ' '.join(words)
    return new_sentence