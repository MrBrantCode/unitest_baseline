"""
QUESTION:
Create a function called `aggregate_vowels` that takes a list of words as input, filters out words that start with a consonant or contain non-alphabetic characters, and returns a dictionary with the count of each vowel (a, e, i, o, u) in the remaining words. The function should be case-insensitive.
"""

def aggregate_vowels(words):
    vowels_count = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    vowels = ['a', 'e', 'i', 'o', 'u']

    for word in words:
        # eliminating words that start with a consonant and words that contain non-alphabetic characters
        if word[0].lower() in vowels and word.isalpha():
            for letter in word.lower():
                if letter in vowels:
                    vowels_count[letter] += 1
                
    return vowels_count