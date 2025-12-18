"""
QUESTION:
Write a function `reverse_sentence` that takes a sentence as input, reverses the order of its words, but excludes any words that start with a vowel and have more than 5 characters. The function should return the modified sentence as a string.
"""

def reverse_sentence(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = sentence.split()
    reversed_sentence = []
    for word in words:
        if len(word) <= 5 or word[0].lower() not in vowels:
            reversed_sentence.append(word)
    reversed_sentence.reverse()
    return ' '.join(reversed_sentence)