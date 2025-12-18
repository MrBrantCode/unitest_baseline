"""
QUESTION:
Write a function `count_vowels(words)` that takes a list of words as input and returns the cumulative count of vowels. The function should only consider words that start with a vowel, end with a consonant, are at least 3 characters long, and contain only alphabetic characters.
"""

def count_vowels(words):
    total_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for word in words:
        if (word[0].lower() in vowels and word[-1].lower() not in vowels and len(word) >= 3) and word.isalpha():
            for letter in word:
                if letter.lower() in vowels:
                    total_vowels += 1
    return total_vowels