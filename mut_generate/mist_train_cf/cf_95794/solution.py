"""
QUESTION:
Write a function `count_letters_vowels_consonants` that takes a string `text` as input. The function should return the count of each letter in the string, disregarding case sensitivity and non-alphabetic characters, as well as the total counts of vowels and consonants. The function should return a tuple containing a dictionary of letter counts, the vowel count, and the consonant count.
"""

def count_letters_vowels_consonants(text):
    text = text.lower()
    text = ''.join(ch for ch in text if ch.isalpha())

    letter_counts = {}
    vowel_count = 0
    consonant_count = 0

    for letter in text:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

        if letter in 'aeiou':
            vowel_count += 1
        else:
            consonant_count += 1

    return letter_counts, vowel_count, consonant_count