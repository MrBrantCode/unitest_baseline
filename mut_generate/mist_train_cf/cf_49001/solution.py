"""
QUESTION:
Create a function named `rearrange_by_vowels` that takes a list of strings as input and returns the list rearranged in ascending order based on the count of vowels in each string. If two strings have the same number of vowels, maintain their original order in the list. The function should be case-insensitive when counting vowels.
"""

def rearrange_by_vowels(strings_list):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count_vowels = [sum([string.lower().count(v) for v in vowels]) for string in strings_list]
    return [x for _, x in sorted(zip(count_vowels, strings_list))]