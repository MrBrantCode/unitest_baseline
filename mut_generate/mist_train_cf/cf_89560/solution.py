"""
QUESTION:
Create a function named `reverse_words` that takes a string as input, reverses each word's alphabetic characters while ignoring non-alphabetic characters, capitalizes the first letter of each reversed word, and returns the resulting string.
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