"""
QUESTION:
Write a function called `reverse_words` that takes a string as input, reverses the order of words in the string, and also reverses each word individually. The function should return the resulting string. The input string may contain punctuation and special characters, which should be treated as part of the word.
"""

def reverse_words(string):
    words = string.split()  
    reversed_words = [word[::-1] for word in words]  
    reversed_string = ' '.join(reversed(reversed_words))  
    return reversed_string