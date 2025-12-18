"""
QUESTION:
Write a function `remove_vowels(sentence)` that takes a sentence as input, removes all vowels from the sentence, converts the remaining letters to uppercase, and returns the modified sentence along with the total count of consonants in the modified sentence. The function should be case-insensitive when removing vowels and should only count alphabetic characters as consonants.
"""

def remove_vowels(sentence):
    """
    Removes all vowels from a sentence, converts the remaining letters to uppercase, 
    and returns the modified sentence along with the total count of consonants.
    
    Args:
    sentence (str): The input sentence.
    
    Returns:
    tuple: A tuple containing the modified sentence and the consonant count.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    modified_sentence = ""
    consonant_count = 0
    
    for letter in sentence:
        if letter.lower() not in vowels:
            modified_sentence += letter.upper()
            if letter.isalpha():
                consonant_count += 1
    
    return modified_sentence, consonant_count