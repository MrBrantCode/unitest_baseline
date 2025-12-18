"""
QUESTION:
Write a function `process_text(s)` that takes a string `s` as input and returns a string after performing the following operations: 
- converting the string to uppercase, 
- removing all numeric characters, and 
- reversing the order of the words in the sentence.
"""

def entrance(s):
    s = s.upper()  
    s = ''.join(c for c in s if not c.isdigit())  
    words = s.split()  
    s = ' '.join(words[::-1])
    return s