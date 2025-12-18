"""
QUESTION:
Write a function named `convert_to_words` that takes an integer `n` as input and returns its English word equivalent. The function should handle numbers from 0 to 10.
"""

# dictionary to convert numbers to words
number_words = {0 : 'zero', 1: 'one', 2 : 'two',
                3 : 'three', 4 : 'four', 5 : 'five', 
                6 : 'six', 7 : 'seven', 8 : 'eight', 
                9 : 'nine', 10 : 'ten'}

def convert_to_words(n):
    if n in number_words:
        return number_words[n]
    return ""