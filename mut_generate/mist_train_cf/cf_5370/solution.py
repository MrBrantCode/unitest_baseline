"""
QUESTION:
Write a function `check_strings` that takes a list of strings as input. The function should check if all strings in the list have the same length and contain only lowercase alphabets. Additionally, it should check if each string contains at least one vowel and at least one consonant. If these conditions are met, the function should return a dictionary where the keys are distinct characters in the strings (excluding whitespace characters) and the values are their respective counts. If any of the conditions are not met, the function should return False.
"""

def check_strings(strings):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}

    # Check if all strings have the same length and contain only lowercase alphabets
    length = len(strings[0])
    for string in strings:
        if len(string) != length or not string.islower():
            return False

    # Check if each string has at least one vowel and one consonant
    for string in strings:
        has_vowel = False
        has_consonant = False
        for char in string:
            if char in vowels:
                has_vowel = True
            elif char in consonants:
                has_consonant = True
        if not has_vowel or not has_consonant:
            return False

    # Count the occurrences of each distinct character, excluding whitespace characters
    char_count = {}
    for string in strings:
        for char in string:
            if char != ' ':
                char_count[char] = char_count.get(char, 0) + 1

    return char_count