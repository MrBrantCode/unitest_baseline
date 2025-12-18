"""
QUESTION:
Write a function `spell_vowels(word)` that takes a string `word` as input and returns a string consisting of all vowels from the input word, in the same order as they appear, with each vowel used only once. The function should be case-insensitive, meaning it should treat both lowercase and uppercase vowels as the same.
"""

def spell_vowels(word):
    vowels = "aeiou"
    result = ""
    used_vowels = set()
    
    for char in word:
        if char.lower() in vowels and char.lower() not in used_vowels:
            result += char.lower()
            used_vowels.add(char.lower())
    
    return result