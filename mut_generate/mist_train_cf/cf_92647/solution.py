"""
QUESTION:
Write a function `reverse_words` that takes a sentence as input, reverses each word that contains at least one vowel, and returns the resulting sentence.
"""

def reverse_words(sentence):
    vowels = "aeiouAEIOU"
    words = sentence.split()
    reversed_words = []
    
    for word in words:
        if any(char in vowels for char in word):
            reversed_words.append(word[::-1])
        else:
            reversed_words.append(word)
    
    return ' '.join(reversed_words)