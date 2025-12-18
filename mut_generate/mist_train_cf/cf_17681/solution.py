"""
QUESTION:
Write a function `find_most_frequent_character(strings)` that takes a list of strings as input and returns the most frequent non-vowel character in the strings, ignoring case sensitivity and spaces. If there are multiple equally frequent characters, return the one that appears first in the list. If all characters in the strings are vowels, return None.
"""

def find_most_frequent_character(strings):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    frequencies = {}

    for string in strings:
        string = string.replace(" ", "").lower()
        for char in string:
            if char in vowels:
                continue
            if char not in frequencies:
                frequencies[char] = 1
            else:
                frequencies[char] += 1

    sorted_freq = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    most_frequent_char = None
    for char, freq in sorted_freq:
        if char not in vowels:
            most_frequent_char = char
            break

    return most_frequent_char