"""
QUESTION:
Write a function `pig_latin(word)` that converts a word into Pig Latin. If the word starts with a vowel, append "way" to the end. If the word starts with a consonant, move the consonant to the end and append "ay". The function should work for words with both lowercase and uppercase letters.
"""

def pig_latin(word):
    """
    Convert a word into Pig Latin.
    
    If the word starts with a vowel, append "way" to the end.
    If the word starts with a consonant, move the consonant to the end and append "ay".
    
    Parameters:
    word (str): The word to convert into Pig Latin.
    
    Returns:
    str: The word in Pig Latin.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0].lower() in vowels:
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"