"""
QUESTION:
Create a function called `remove_vowels` that takes a sentence as input, removes all vowels from the sentence, and returns the modified sentence. The sentence may contain punctuation marks, special characters, and multiple spaces between words.
"""

def remove_vowels(sentence):
    vowels = "aeiouAEIOU"
    modified_sentence = ""
    for char in sentence:
        if char not in vowels:
            modified_sentence += char
    return modified_sentence