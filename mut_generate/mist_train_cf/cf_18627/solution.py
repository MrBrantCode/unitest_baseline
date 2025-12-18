"""
QUESTION:
Create a function named `count_vowels` that takes a list of strings as input and returns a dictionary. The dictionary's keys should be the input strings, and the values should be the number of vowels in each string. The dictionary should be sorted by the number of vowels in descending order, and if two strings have the same number of vowels, they should be sorted alphabetically.
"""

def count_vowels(strings):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_counts = {}
    for string in strings:
        count = 0
        for char in string:
            if char.lower() in vowels:
                count += 1
        vowel_counts[string] = count
    sorted_vowel_counts = dict(sorted(vowel_counts.items(), key=lambda x: (-x[1], x[0])))
    return sorted_vowel_counts