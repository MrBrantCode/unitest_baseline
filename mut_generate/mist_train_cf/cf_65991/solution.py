"""
QUESTION:
Write a function `sort_dict_by_vowels` that sorts a dictionary by the number of vowels in each key. The keys are strings.
"""

def sort_dict_by_vowels(dictionary):
    return {k: v for k, v in sorted(dictionary.items(), key=lambda item: sum(1 for char in item[0].lower() if char in 'aeiou'))}