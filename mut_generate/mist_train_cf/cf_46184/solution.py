"""
QUESTION:
Create a function `compare_vowel_consonant_sets` that takes two string parameters and returns a boolean value. The function should compare the sets of vowels and consonants in the two strings, ignoring case, position, and non-alphabetic characters, and return True if the sets of vowels and consonants are identical and their frequencies are equal, and False otherwise.
"""

def compare_vowel_consonant_sets(string1: str, string2: str) -> bool:
    string1 = string1.lower()
    string2 = string2.lower()

    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = set("bcdfghjklmnpqrstvwxyz")

    string1_chars = set(char for char in string1 if char.isalpha())
    string2_chars = set(char for char in string2 if char.isalpha())
    
    string1_vowels = {char for char in string1_chars if char in vowels}
    string1_consonants = {char for char in string1_chars if char in consonants}

    string2_vowels = {char for char in string2_chars if char in vowels}
    string2_consonants = {char for char in string2_chars if char in consonants}

    if string1_vowels == string2_vowels and string1_consonants == string2_consonants:
        string1_vowel_counts = {vowel: string1.count(vowel) for vowel in string1_vowels}
        string2_vowel_counts = {vowel: string2.count(vowel) for vowel in string2_vowels}

        string1_consonants_counts = {consonant: string1.count(consonant) for consonant in string1_consonants}
        string2_consonants_counts = {consonant: string2.count(consonant) for consonant in string2_consonants}

        return string1_vowel_counts == string2_vowel_counts and string1_consonants_counts == string2_consonants_counts
    else:
        return False