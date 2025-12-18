"""
QUESTION:
Write a function `reverse_words(s)` that takes a string `s` as input and returns a new string where the characters in each word of `s` are reversed. The function should split the input string into words, reverse the characters in each word, and then join the reversed words back together with spaces in between.
"""

def reverse_words(s):
    # Split the string into a list of words
    words = s.split()
    
    # Reverse the characters in each word
    reversed_words = [word[::-1] for word in words]
    
    # Join the reversed words back together
    result = ' '.join(reversed_words)
    
    return result