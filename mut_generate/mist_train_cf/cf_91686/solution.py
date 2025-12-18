"""
QUESTION:
Create a function called `contains_all_vowels_in_order` that takes a string as input and returns a boolean indicating whether the string contains all the vowels ('a', 'e', 'i', 'o', 'u') in alphabetical order, regardless of case and presence of other characters.
"""

def contains_all_vowels_in_order(string):
    vowels = "aeiou"
    vowel_index = 0

    for char in string:
        if char.lower() == vowels[vowel_index]:
            vowel_index += 1
            if vowel_index == len(vowels):
                return True

    return False