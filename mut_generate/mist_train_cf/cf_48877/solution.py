"""
QUESTION:
Construct a function named `count_vowels` that takes a list of words as input. The function should return the cumulative count of vowels from the input list, but only consider words that start with a vowel and contain only alphabetic characters. The function should handle words with both lowercase and uppercase letters.
"""

def count_vowels(words):
    total_vowels = 0
    vowels = 'aeiou'
    for word in words:
        if word[0].lower() in vowels and word.isalpha():
            total_vowels += sum(letter.lower() in vowels for letter in word)
    return total_vowels