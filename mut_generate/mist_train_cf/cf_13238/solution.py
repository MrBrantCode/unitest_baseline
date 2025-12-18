"""
QUESTION:
Write a function called `sort_words` to sort a list of words in descending order based on their lengths. If multiple words have the same length, sort them in alphabetical order. The function should return the sorted list.
"""

def sort_words(word_list):
    return sorted(word_list, key=lambda x: (-len(x), x))