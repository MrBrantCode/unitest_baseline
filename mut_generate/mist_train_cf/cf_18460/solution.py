"""
QUESTION:
Create a function `unique_words_with_vowel` that takes a string of space-separated words as input and returns a list of unique words that contain at least one vowel but do not start with a vowel. The output list should be sorted in alphabetical order and the function should be case-sensitive.
"""

def unique_words_with_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = string.split()
    unique_words = set()
    
    for word in words:
        if word[0].lower() in vowels:
            continue
        for char in word:
            if char.lower() in vowels:
                unique_words.add(word)
                break
    
    return sorted(list(unique_words))