"""
QUESTION:
Write a function `extract_words(sentence, letter)` that extracts all words from a given sentence that begin with a specific letter, have a length greater than or equal to 3, and contain at least one vowel. The function should be case-insensitive when checking the letter and vowels.
"""

def entrance(sentence, letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = sentence.split()
    extracted_words = []
    
    for word in words:
        if word[0].lower() == letter.lower() and len(word) >= 3 and any(vowel in word.lower() for vowel in vowels):
            extracted_words.append(word)
    
    return extracted_words