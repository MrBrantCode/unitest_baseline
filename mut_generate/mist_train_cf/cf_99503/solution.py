"""
QUESTION:
Create a function called `sentence_type(sentence)` that takes a sentence as input and returns whether it is "affirmative", "negative", or "neutral". The function should determine the sentence type by comparing the number of vowels (excluding 'y') and consonants (excluding 'y') in the sentence. If the number of vowels is greater than the number of consonants, return "affirmative". If the number of consonants is greater than the number of vowels, return "negative". If the number of vowels and consonants are equal, return "neutral".
"""

def sentence_type(sentence):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    num_vowels = sum(sentence.lower().count(v) for v in vowels)
    num_consonants = sum(sentence.lower().count(c) for c in consonants)
    if num_vowels > num_consonants:
        return "affirmative"
    elif num_vowels < num_consonants:
        return "negative"
    else:
        return "neutral"