"""
QUESTION:
Given a list of words and a target word, write a function `find_word` that returns the index of the target word in the list. If the target word is not found, return the index of the first word that starts with the same letter as the target word. If no such word is found, return -1.
"""

def find_word(list_words, target_word):
    for i, word in enumerate(list_words):
        if word == target_word:
            return i
        if word[0] == target_word[0]:
            return i
    return -1