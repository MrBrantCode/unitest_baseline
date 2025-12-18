"""
QUESTION:
Design a function `remove_vowels_duplicates_sort(string)` to process a string of up to 100 characters. The function should remove all vowels from the string, eliminate duplicate characters, and return the remaining characters sorted in descending order of their ASCII values.
"""

def remove_vowels_duplicates_sort(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_removed = ''.join([char for char in string if char not in vowels])
    unique_chars = ''.join(set(vowels_removed))
    sorted_chars = sorted(unique_chars, key=lambda x: ord(x), reverse=True)
    return ''.join(sorted_chars)