"""
QUESTION:
Create a function `count_characters` that takes a string as input and returns the total count of alphabetic characters (ignoring case), the total count of words (split by whitespace), and the frequency of each character (including special characters and punctuation marks) in descending order of frequency.
"""

from collections import Counter

def count_characters(s):
    # Count total alphabetic characters and words
    total_characters = sum(1 for c in s if c.isalpha())
    total_words = len(s.split())

    # Count frequency of each character
    character_frequency = Counter(s)

    # Sort characters based on frequency in descending order
    sorted_characters = sorted(character_frequency.items(), key=lambda x: x[1], reverse=True)

    return total_characters, total_words, dict(sorted_characters)