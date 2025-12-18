"""
QUESTION:
Create a function called `contains_all_vowels_in_order` that checks if a given string contains all the vowels ('a', 'e', 'i', 'o', 'u') in alphabetical order. The function should be case-insensitive and return True if the string contains all vowels in alphabetical order, False otherwise.
"""

def contains_all_vowels_in_order(string):
    vowels = "aeiou"
    vowel_index = 0

    for char in string.lower():
        if char == vowels[vowel_index]:
            vowel_index += 1
            if vowel_index == len(vowels):
                return True

    return False