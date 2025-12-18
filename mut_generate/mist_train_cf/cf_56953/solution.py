"""
QUESTION:
Design a function called `uncommon_vowel_finder` that takes a list of strings as input. The function should disregard capitalization and return True if more than one distinct string in the list ends with either 'u' or 'y', and False otherwise. The strings must end with 'u' or 'y' only, without any additional characters after the vowel.
"""

def uncommon_vowel_finder(lst):
    words = set([word.lower() for word in lst if word.lower().endswith(('u', 'y'))])
    return len(words)>1