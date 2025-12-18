"""
QUESTION:
Write a function called `count_e` that takes in a string input and returns the total count of the letter 'e' (both upper and lower case) in the input string. The function should be able to handle multiple sentences, punctuations, and special characters.
"""

def count_e(input_string):
    input_string = input_string.lower()
    e_count = input_string.count('e')
    return e_count