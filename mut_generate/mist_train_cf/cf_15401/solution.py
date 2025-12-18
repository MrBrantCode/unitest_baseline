"""
QUESTION:
Write a function `reverse_words` that takes a string as input and returns a string where each word's alphabetic characters are reversed, ignoring non-alphabetic characters and maintaining the original word order.
"""

def reverse_words(string):
    words = string.split()  # Split the string into a list of words
    reversed_words = []
    
    for word in words:
        # Remove punctuation marks and special characters
        cleaned_word = ''.join(char for char in word if char.isalpha())
        reversed_words.append(cleaned_word[::-1])  # Reverse the word and add it to the reversed_words list
    
    return ' '.join(reversed_words)  # Join the reversed words back into a string with spaces as separators