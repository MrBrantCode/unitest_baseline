"""
QUESTION:
Create a function called `convert_to_plural_uppercase` that takes a sentence as input, converts it to plural form by adding "es" to the word "one" and "s" to the word "friend", capitalizes the first letter of the sentence, adds a punctuation mark at the end if none exists, and converts all letters to uppercase.
"""

def convert_to_plural_uppercase(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace('one', 'ones').replace('friend', 'friends')
    sentence = sentence.strip('.!?').capitalize() + '.'
    sentence = sentence.upper()
    return sentence