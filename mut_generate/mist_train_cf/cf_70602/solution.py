"""
QUESTION:
Write a function `piglatin_translator` that takes a string `character_sequence` as input. The function should translate the input string into Pig Latin. In Pig Latin, if the first letter of a word is a vowel, the translation is the original word followed by "way". If the first letter is not a vowel, the translation is the rest of the word followed by the first letter and then "ay". The function should return the translated string, with all translated words separated by spaces.
"""

def piglatin_translator(character_sequence):
    vowels = ['a', 'e', 'i', 'o', 'u'] 
    piglatin = ""
    
    for word in character_sequence.split():
        first_letter = word[0]
        
        if first_letter.lower() in vowels:
            piglatin += f"{word}way "
        else:
            piglatin += f"{word[1:]}{first_letter}ay "
    
    return piglatin.strip()