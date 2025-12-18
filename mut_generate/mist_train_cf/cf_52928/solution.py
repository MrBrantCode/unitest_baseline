"""
QUESTION:
Write a function `analyze_char(s)` that accepts a string `s` and returns a dictionary showing the counts of different vowels, consonants, and special characters in the string. The function should be case-insensitive, and vowels only include 'a', 'e', 'i', 'o', and 'u'. The output dictionary should have the format: {'A': <count>, 'E': <count>, 'I': <count>, 'O': <count>, 'U': <count>, 'Consonants': <count>, 'Special characters': <count>}.
"""

def analyze_char(s):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowel_dict = {char: 0 for char in vowels.upper()}
    count_dict = {'Consonants': 0, 'Special characters': 0}
    count_dict.update(vowel_dict)

    for char in s.lower():
        if char in vowels:
            count_dict[char.upper()] += 1
        elif char in consonants:
            count_dict['Consonants'] += 1
        else:
            count_dict['Special characters'] += 1

    return count_dict