"""
QUESTION:
Write a function called `calculate_unicode_sum` that takes a string as input and returns the sum of the Unicode values of all characters in the string. The function should add the Unicode value of each letter (a-z and A-Z) to the sum, and subtract the Unicode value of each non-letter character.
"""

def calculate_unicode_sum(input_string):
    sum_unicode = 0
    for char in input_string:
        if char.isalpha():
            sum_unicode += ord(char)
        else:
            sum_unicode -= ord(char)
    return sum_unicode