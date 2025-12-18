"""
QUESTION:
Write a function named `reverse_words` that takes a string of alphabetic characters and spaces as input, reverses the order of the words, and then reverses the characters within each word, maintaining the original capitalization. The function should return the modified string.
"""

def reverse_words(s):
    # Split the string into a list of words
    words = s.split()
    
    # Reverse the order of words
    words = words[::-1]
    
    # Reverse the characters within each word
    reversed_words = [word[::-1] for word in words]
    
    # Join the words back together with spaces
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string