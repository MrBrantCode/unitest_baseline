"""
QUESTION:
Write a function named `count_vowels` that takes a string as input and returns a dictionary with the count of each unique vowel ('a', 'e', 'i', 'o', 'u') in the string, ignoring case. If no vowels are found, return an empty dictionary. The function should have a time complexity of O(n), where n is the length of the string.
"""

def count_vowels(s):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for char in s:
        if char.lower() in vowels:
            vowels[char.lower()] += 1
    return {k: v for k, v in vowels.items() if v > 0}