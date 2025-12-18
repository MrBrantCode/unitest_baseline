"""
QUESTION:
Write a function `find_most_frequent_character(strings)` that finds the most frequent character in a given list of strings, ignoring case sensitivity and spaces, and excluding vowels. If there are multiple most frequent characters, return the one that appears first in the list. If all characters are vowels, return None. If all characters are non-vowels, return the most frequent character regardless of being a vowel or not.
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