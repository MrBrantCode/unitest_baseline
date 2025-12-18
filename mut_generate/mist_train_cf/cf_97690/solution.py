"""
QUESTION:
Extract Hidden Message Function: 

Create a function `extract_hidden_message` that takes a string as input and returns a string containing every second letter starting from the second letter of the input string. The function should utilize Python string slicing.
"""

def extract_hidden_message(string):
    return string[1::2]