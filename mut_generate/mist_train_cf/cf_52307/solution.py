"""
QUESTION:
Develop a function named `get_sentence_type` that takes a sentence as input and returns the sentence type as either "Declarative", "Interrogative", "Exclamatory", or "Imperative". The function should use the sentence's punctuation to determine its type, specifically: '?' for Interrogative, '!' for Exclamatory, and the first word's capitalization for Imperative. If none of these conditions apply, the sentence is considered Declarative. Note that this solution assumes proper punctuation in the input sentence.
"""

def get_sentence_type(sentence):
    if sentence.endswith('?'):
        return "Interrogative"
    elif sentence.endswith('!'):
        return "Exclamatory"
    elif sentence.istitle():
        return "Imperative"
    else:
        return "Declarative"