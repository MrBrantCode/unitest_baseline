"""
QUESTION:
Create a function `remove_middle_word` that takes a string sentence as input and returns the sentence with the middle word removed. The sentence will always have an odd number of words (at least 5), no punctuation marks, numbers, or spaces within words, and all letters will be lowercase.
"""

def remove_middle_word(sentence):
    words = sentence.split()
    middle_index = len(words) // 2
    words.pop(middle_index)
    new_sentence = ' '.join(words)
    return new_sentence