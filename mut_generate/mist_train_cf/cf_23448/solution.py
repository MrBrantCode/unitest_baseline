"""
QUESTION:
Create a function `remove_vowels(string)` that takes an input string and returns a new string with all the vowels ('a', 'e', 'i', 'o', 'u') removed, ignoring the case of the vowels.
"""

def remove_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    new_string = ""
    for letter in s:
        if letter.lower() not in vowels:
            new_string += letter
    return new_string