"""
QUESTION:
Create a function `char_count(s)` that takes a string `s` as input and returns a dictionary containing the counts of vowels, consonants, and special characters, as well as the frequency of each vowel and consonant. The function should be case-insensitive and consider only alphabets and special characters. The output dictionary should have the following format: `{'Vowels': {...}, 'Consonants': {...}, 'Special characters': ...}`, where `...` represents the frequency of each vowel or consonant, and the count of special characters respectively.
"""

def char_count(s):
    counts = {"Vowels": {}, "Consonants": {}, "Special characters": 0}
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    for char in s:
        char_lower = char.lower()
        if char_lower in vowels:
            counts["Vowels"][char_lower] = counts["Vowels"].get(char_lower, 0) + 1
        elif char_lower in consonants:
            counts["Consonants"][char_lower] = counts["Consonants"].get(char_lower, 0) + 1
        elif not char.isalnum():
            counts["Special characters"] += 1

    return counts