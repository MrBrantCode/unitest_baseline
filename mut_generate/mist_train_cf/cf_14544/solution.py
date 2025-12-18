"""
QUESTION:
Write a Python function named `count_strings` that takes a list of strings and a single character as input. The function should return a dictionary where the keys are the strings that contain the character and the values are the count of occurrences. The function should consider each string case-insensitively and ignore strings that contain special characters or numbers. If the character is a vowel, only vowels in the strings should be considered; if the character is a consonant, only consonants in the strings should be considered.
"""

def count_strings(strings, character):
    count_dict = {}
    for string in strings:
        if character.lower() in string.lower():
            if character.lower() in 'aeiou':
                count = string.lower().count(character.lower())
                if string.isalpha():
                    count_dict[string] = count
            else:
                consonants = ''.join([c for c in string.lower() if c.isalpha() and c not in 'aeiou'])
                count = consonants.count(character.lower())
                count_dict[string] = count
    return count_dict