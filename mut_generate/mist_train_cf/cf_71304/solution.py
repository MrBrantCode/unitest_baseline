"""
QUESTION:
Create a function `count_vowels` that takes a list of words as input, and returns the total count of vowels from the words that start with a vowel and contain only alphabetic characters.
"""

def count_vowels(words):
    total_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_words = [word for word in words if word[0].lower() in vowels and word.isalpha()]
    for word in filtered_words:
        for letter in word.lower():
            if letter in vowels:
                total_vowels += 1
    return total_vowels