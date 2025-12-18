"""
QUESTION:
Create a function named `convert_sentence(sentence)` that takes a sentence as input and returns a list of words. The function should exclude any words that start with a vowel (a, e, i, o, u) and contain more than three letters, and sort the resulting list in alphabetical order.
"""

def convert_sentence(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = sentence.split()
    result = []
    
    for word in words:
        if word[0].lower() not in vowels and len(word) <= 3:
            result.append(word)
    
    result.sort()
    return result