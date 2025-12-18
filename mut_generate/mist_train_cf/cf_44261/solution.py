"""
QUESTION:
Implement a function `custom_sort` that sorts an array of strings in ascending lexicographical order with the following exceptions: 
- strings starting with a vowel ('a', 'e', 'i', 'o', 'u') should come before strings starting with a non-vowel, 
- consider case-insensitivity when determining if a string starts with a vowel. 
Do not use any built-in sorting functions.
"""

def custom_sort(array):
    array.sort(key=lambda x: (x[0].lower() not in 'aeiou', x.lower()))
    return array