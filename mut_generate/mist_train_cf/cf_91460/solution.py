"""
QUESTION:
Write a function called `reverse_sentence` that takes a string of words as input. The function should return a string where the order of the words is reversed, excluding any words that start with a vowel (case-insensitive) and have more than 5 characters.
"""

def reverse_sentence(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = sentence.split()
    reversed_sentence = [word for word in words if len(word) <= 5 or word[0].lower() not in vowels]
    return ' '.join(reversed(reversed_sentence))