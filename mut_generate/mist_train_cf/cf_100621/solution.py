"""
QUESTION:
Create a function `sentence_type(sentence)` that takes a sentence as input and returns whether the sentence is "affirmative", "negative", or "neutral" based on the count of vowels and consonants (excluding 'y'). The sentence type is determined as follows: affirmative if vowels > consonants, negative if vowels < consonants, and neutral if vowels = consonants. The function should ignore non-alphabetic characters and case-insensitive.
"""

def sentence_type(sentence):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    sentence = sentence.lower()
    num_vowels = sum(sentence.count(v) for v in vowels)
    num_consonants = sum(sentence.count(c) for c in consonants)
    if num_vowels > num_consonants:
        return "affirmative"
    elif num_vowels < num_consonants:
        return "negative"
    else:
        return "neutral"