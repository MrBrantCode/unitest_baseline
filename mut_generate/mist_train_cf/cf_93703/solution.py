"""
QUESTION:
Write a function called `reverse_words` that takes a string as input and returns a string where each word has been reversed, while keeping the order of the words intact and ignoring any punctuation marks and special characters.
"""

def reverse_words(string):
    words = string.split()  
    reversed_words = []
    
    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalpha())
        reversed_words.append(cleaned_word[::-1])  
    
    return ' '.join(reversed_words) 