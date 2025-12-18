"""
QUESTION:
Create a function `sort_by_vowels` that takes an array of strings as input and returns a new array of strings sorted first by the number of vowels in each string and then by the length of the string.
"""

def sort_by_vowels(arr):
    def count_vowels(s):
        vowels = "aeiouAEIOU"
        return len([c for c in s if c in vowels])

    return sorted(arr, key=lambda s: (count_vowels(s), len(s)))