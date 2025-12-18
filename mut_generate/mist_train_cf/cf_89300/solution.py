"""
QUESTION:
Write a function `count_unique_vowels` that takes a list of strings as input. The function should convert each string to lowercase, concatenate them into a single string, and return the number of unique vowels in the resulting string. The function should ignore duplicate vowels and only consider unique vowels in the count.
"""

def count_unique_vowels(list_of_strings):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    concatenated_string = ''.join(list_of_strings).lower()
    unique_vowels = set([c for c in concatenated_string if c in vowels])
    return len(unique_vowels)