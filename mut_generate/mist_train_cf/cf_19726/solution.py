"""
QUESTION:
Write a function `count_letters_vowels_consonants` that takes a string as input and returns a tuple containing three values: 
- A dictionary with the count of each alphabetic character in the string (case-insensitive and excluding non-alphabetic characters).
- The total count of vowels in the string (case-insensitive).
- The total count of consonants in the string (case-insensitive).

The function should disregard case sensitivity and exclude any non-alphabetic characters from the count.
"""

def count_letters_vowels_consonants(text):
    text = text.lower()  # Convert to lowercase
    text = ''.join(ch for ch in text if ch.isalpha())  # Remove non-alphabetic characters

    letter_counts = {}  # Dictionary to store letter counts
    vowel_count = 0  # Count of vowels
    consonant_count = 0  # Count of consonants

    for letter in text:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

        if letter in 'aeiou':  # Check if letter is a vowel
            vowel_count += 1
        else:
            consonant_count += 1

    return letter_counts, vowel_count, consonant_count