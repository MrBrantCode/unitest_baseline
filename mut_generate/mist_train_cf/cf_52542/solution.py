"""
QUESTION:
Write a function `count_vowels_and_z` that checks if a string contains any of the vowels ('a', 'e', 'i', 'o', 'u') or the letter 'z' in the middle (excluding the start and end of the word), in a case-insensitive manner. The function should return a boolean indicating the presence of these characters and an integer representing the count of these characters in the middle of the string.
"""

def count_vowels_and_z(word):
    vowels = 'aeiouz'
    word = word.lower()[1:-1]
    count = sum(letter in vowels for letter in word)
    return count > 0, count