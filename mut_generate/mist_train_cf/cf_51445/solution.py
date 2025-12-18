"""
QUESTION:
Write a function `extract_data(str)` that takes a string `str` as input and returns the following: 
If the string contains spaces or semicolons, return a list of substrings separated by these separators.
If the string does not contain spaces or semicolons, calculate the number of uppercase letters at even indices (0-based numbering) and the sum of all odd numbers in the string, and return their sum.
Prioritize the separator operation if both separators and numbers are present in the string.
"""

import re

def extract_data(str):
    if ' ' in str or ';' in str:
        return re.split(' |;', str)
    else:
        upper_case_count = sum(1 for i in range(len(str)) if str[i].isupper() and i%2==0)
        digits_sum = sum(int(i) for i in str if i.isdigit() and int(i)%2!=0)
        return upper_case_count + digits_sum