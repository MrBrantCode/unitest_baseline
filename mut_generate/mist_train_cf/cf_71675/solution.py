"""
QUESTION:
Implement a function `sort_phrases(phrases)` that sorts a list of phrases in ascending order based on the number of words in each phrase. If two or more phrases have the same word count, they should be sorted alphabetically by their first word in a case-insensitive manner. The function should modify the input list and return the sorted list of phrases. Do not use built-in Python functions that directly solve this task, and ensure the solution handles case sensitivity properly.
"""

def sort_phrases(phrases):
    phrases.sort(key=lambda phrase: (len(phrase.split()), phrase.split()[0].lower()))
    return phrases