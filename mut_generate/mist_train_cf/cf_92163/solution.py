"""
QUESTION:
Write a function named `sum_of_alphabetic_characters` that calculates the sum of all alphabetic characters in a given string. The sum is calculated by assigning a numerical value to each letter, where 'a' is 1, 'b' is 2, and so on, regardless of case. Non-alphabetic characters are excluded from the sum. The function should take a string as input and return the calculated sum.
"""

def sum_of_alphabetic_characters(s):
    return sum(ord(char.lower()) - 96 for char in s if char.isalpha())