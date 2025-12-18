"""
QUESTION:
Create a function named `sort_by_last_letter` that takes a list of words as input and returns the list sorted based on the last letter of each word. If two words have the same last letter, they should be sorted by the second last letter. If these second to last letters are also the same, the words should be sorted by the third last letter, and so on. If the words are identical, retain the original order. The function should maintain good performance even when dealing with large lists.
"""

def sort_by_last_letter(words):
    return sorted(words, key=lambda word: (word[::-1], words.index(word)))