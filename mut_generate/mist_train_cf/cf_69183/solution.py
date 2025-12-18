"""
QUESTION:
Write a function `sort_words` that sorts a list of words in ascending order based on the second character of each word. The function should take a list of words as input and return the sorted list. The function should be able to handle words of varying lengths, including words with fewer than two characters. If a word has fewer than two characters, it should be placed at the beginning of the sorted list.
"""

def sort_words(words):
    words.sort(key=lambda word: word[1:] if len(word) > 1 else '')
    return words