"""
QUESTION:
Create a function `find_palindromes` that takes a string `text` as input and returns a list of all palindromic numerals found in the string. A palindromic numeral is a number that reads the same forwards and backwards. The function should be able to find palindromic numerals of any length.
"""

import re

def find_palindromes(text):
    num_list = re.findall('\d+', text)
    palindromes = [num for num in num_list if num == num[::-1]]
    return palindromes