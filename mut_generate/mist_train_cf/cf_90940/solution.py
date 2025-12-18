"""
QUESTION:
Given a string of no more than 1000 characters, write a function called `find_longest_word_with_vowel` that returns the word with the longest length that contains at least one vowel.
"""

def find_longest_word_with_vowel(string):
    vowels = "aeiou"
    longest_word = ""
    max_length = 0

    # Split the string into words
    words = string.split()

    # Iterate through each word
    for word in words:
        # Check if the word contains at least one vowel
        if any(vowel in word.lower() for vowel in vowels):
            # If the length of the word is longer than the current longest word, update the longest word
            if len(word) > max_length:
                max_length = len(word)
                longest_word = word

    return longest_word