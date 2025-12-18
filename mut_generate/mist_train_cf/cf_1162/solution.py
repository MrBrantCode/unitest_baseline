"""
QUESTION:
Create a function named `sort_strings_by_vowels` that takes an array of strings as input and returns a new array of strings. The returned array should be sorted by the number of vowels in each string in ascending order, and then by the length of the string in ascending order. The function should only consider strings that have at least 3 characters and contain at least one consonant, ignoring case when counting vowels and checking for consonants.
"""

def sort_strings_by_vowels(arr):
    def count_vowels(word):
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for char in word.lower():
            if char in vowels:
                count += 1
        return count

    filtered_arr = [word for word in arr if len(word) >= 3 and any(char.lower() not in 'aeiou' for char in word)]
    return sorted(filtered_arr, key=lambda x: (count_vowels(x), len(x)))