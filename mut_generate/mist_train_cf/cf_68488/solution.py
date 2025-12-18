"""
QUESTION:
Write a function `detect_e_word_frequency` that takes a list of strings `word_list` as input. The function should return a list of tuples, where each tuple contains a word from the input list that has at least one 'e' and the frequency of 'e' in that word. The function should exclude words without any 'e'.
"""

def detect_e_word_frequency(word_list):
    e_words = []
    for word in word_list:
        if 'e' in word:
            e_words.append((word, word.count('e')))
    return e_words