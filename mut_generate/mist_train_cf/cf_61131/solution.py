"""
QUESTION:
Create a function `is_all_words_english` that checks if all words in a given list are recognized by a provided English lexicon. The function should return `True` if all words are authentic English words, and `False` otherwise. The function should take two parameters: `word_list` (the list of words to be checked) and `english_lexicon` (a set of recognized English words).
"""

def is_all_words_english(word_list, english_lexicon):
    for word in word_list:
        if word not in english_lexicon:
            return False
    return True