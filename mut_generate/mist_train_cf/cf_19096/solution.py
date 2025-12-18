"""
QUESTION:
Write a function `replace_vowels_with_asterisks(sentence)` that takes a sentence as input, replaces all vowels (both lowercase and uppercase) with asterisks, and returns the modified sentence.
"""

def replace_vowels_with_asterisks(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    modified_sentence = ""
    
    for char in sentence:
        if char in vowels:
            modified_sentence += '*'
        else:
            modified_sentence += char
    
    return modified_sentence