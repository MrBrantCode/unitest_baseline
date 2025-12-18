"""
QUESTION:
Write a function `find_vowel_differences` that takes two strings as input and returns a list of vowels that are different at the same position in both strings. The function should consider only the vowels 'a', 'e', 'i', 'o', 'u' and their uppercase counterparts. If the strings are of different lengths, the function should stop comparing at the end of the shorter string.
"""

def find_vowel_differences(string1, string2):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    differences = []

    for char1, char2 in zip(string1, string2):
        if char1 in vowels and char2 in vowels and char1 != char2:
            differences.append(char1)

    return differences