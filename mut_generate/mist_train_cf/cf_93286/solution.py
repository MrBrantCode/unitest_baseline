"""
QUESTION:
Write a function `count_strings(strings, character)` that takes a list of strings and a single character as input. The function should return a dictionary where the keys are the strings containing the given character and the values are the count of occurrences. The function should consider each string case-insensitively, ignore strings containing special characters or numbers, and only consider vowels if the character is a vowel, and only consider consonants if the character is a consonant.
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