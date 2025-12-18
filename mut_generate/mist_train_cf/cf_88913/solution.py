"""
QUESTION:
Write a function `check_strings(strings)` that takes a list of strings as input. All strings in the list must have the same length and contain only lowercase alphabets. Each string must also contain at least one vowel and one consonant. The function should return a dictionary where the keys are distinct characters (excluding whitespace) and the values are their respective counts across all strings.
"""

def entance(strings):
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