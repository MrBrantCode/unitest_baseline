"""
QUESTION:
Write a function `reverse_words` that takes a string `s` as input, reverses the characters in each word, and returns the resulting string. The input string contains one or more words separated by a space, and the function should return a string where each word's characters are reversed, with the same word order as the input string.
"""

def reverse_words(s):
    # Split the string into a list of words
    words = s.split()
    
    # Reverse the characters in each word
    reversed_words = [word[::-1] for word in words]
    
    # Join the reversed words back together
    result = ' '.join(reversed_words)
    
    return result