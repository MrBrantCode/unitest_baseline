"""
QUESTION:
Design a function `remove_non_alphabetical_chars` that takes a sentence as input and returns the sentence with all non-alphabetical characters removed, excluding spaces. The function should be able to handle sentences with letters and special characters from any language recognized by Python's built-in `isalpha()` function.
"""

def remove_non_alphabetical_chars(sentence):
    # Using list comprehension to find all alphabet characters and join them into new result string.
    result = ''.join(c for c in sentence if c.isalpha() or c.isspace())
    
    # return the result
    return result