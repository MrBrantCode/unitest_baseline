"""
QUESTION:
Create a function named `count_vowels` that takes a list of words as input and returns the total number of vowels in the words that start with a vowel and contain only alphabetic characters. The function should exclude words that start with a consonant and words that contain non-alphabetic characters.
"""

def count_vowels(words):
    total_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for word in words:
        if word[0].lower() not in vowels or not word.isalpha():
            continue
        else:
            for letter in word.lower():
                if letter in vowels:
                    total_vowels += 1
    return total_vowels