"""
QUESTION:
Create a function called `remove_vowels` that takes a sentence as input, removes all lowercase and uppercase vowels from the sentence, and returns the modified sentence. The function should handle punctuation marks, special characters, multiple spaces between words, and edge cases where the sentence is empty or consists of only vowels.
"""

def remove_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    modified_sentence = ""
    for char in sentence:
        if char not in vowels:
            modified_sentence += char
    return modified_sentence