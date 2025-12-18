"""
QUESTION:
Create a function named `compare_vowel_sets` that takes two string parameters. The function should evaluate whether two input strings contain identical sets of vowels, disregarding case, position, and non-alphabetic characters. It must also compare the frequency of the vowels within the strings. The function should return `True` if the strings have identical vowel sets with similar frequency and `False` otherwise.
"""

def compare_vowel_sets(string1: str, string2: str) -> bool:
    vowel_counts1 = {vowel: string1.lower().count(vowel) for vowel in 'aeiou'}
    vowel_counts2 = {vowel: string2.lower().count(vowel) for vowel in 'aeiou'}
    return vowel_counts1 == vowel_counts2