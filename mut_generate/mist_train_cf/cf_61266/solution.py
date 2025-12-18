"""
QUESTION:
Create a function `reverse_words` that takes a string `s` as input, converts it to lower case, and reverses the order of the words while maintaining the original position of spaces, punctuation, and special characters.
"""

def reverse_words(s):
    s = s.lower() 
    words = s.split(" ") 
    words = words[::-1] 
    reversed_s = " ".join(words) 
    
    return reversed_s