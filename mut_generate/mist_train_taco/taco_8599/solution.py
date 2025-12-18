"""
QUESTION:
**This Kata is intended as a small challenge for my students**

Create a function, called ``removeVowels`` (or ``remove_vowels``), that takes a string argument and returns that same string with all vowels removed (vowels are "a", "e", "i", "o", "u").
"""

def remove_vowels(s: str) -> str:
    REMOVE_VOWS = str.maketrans('', '', 'aeiouAEIOU')  # Including uppercase vowels
    return s.translate(REMOVE_VOWS)