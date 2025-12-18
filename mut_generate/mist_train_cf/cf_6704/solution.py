"""
QUESTION:
Write a function called `reverse_words` that takes a string as input, reverses each word, and capitalizes the first letter of each reversed word, ignoring non-alphabetic characters.
"""

def reverse_words(string):
    words = string.split()  
    reversed_words = []  

    for word in words:
        word = ''.join(char for char in word if char.isalpha())
        reversed_word = word[::-1].capitalize()
        reversed_words.append(reversed_word)

    reversed_string = ' '.join(reversed_words)
    return reversed_string