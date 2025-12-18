"""
QUESTION:
Create a function called `less_used_consonants` that takes a list of strings as input and returns a boolean value. The function should ignore punctuation, be case-insensitive, and check if more than one unique string in the list starts with either 'k' or 'z' as the first character, excluding strings that have other characters before 'k' or 'z'. The function should return True if the condition is met and False otherwise.
"""

import string

def less_used_consonants(lst):
    count = 0
    unique_items = []
    for word in lst:
        word = word.lower().translate(str.maketrans('', '', string.punctuation))
        if (word.startswith('k') or word.startswith('z')) and word not in unique_items:
            unique_items.append(word)
            count += 1
    if count > 1:
        return True
    return False