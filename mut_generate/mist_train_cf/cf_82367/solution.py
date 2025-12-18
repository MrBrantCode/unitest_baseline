"""
QUESTION:
Create a function named `extract_data_enhanced` that takes a string as input. The function should first split the string into an array of components based on spaces, commas, semicolons, and asterisks as separators. If the string cannot be split, it should then check the string's contents. If the string contains only uppercase alphabetic characters, the function should return the count of characters with an even index. If the string contains mixed characters, the function should return a dictionary with the count of each character type (uppercase, lowercase, numeric, others) and the most frequent character.
"""

import re
from collections import Counter

def extract_data_enhanced(string):
    string = re.split('[ *,;]',string) 
    if len(string)>1: return string 
    string = string[0]
    if string.isupper():
        return len([char for index,char in enumerate(string) if index % 2 == 0])
    else:
        dict_result = {}
        dict_result['upper'] = sum(1 for ch in string if ch.isupper())
        dict_result['lower'] = sum(1 for ch in string if ch.islower())
        dict_result['digits'] = sum(1 for ch in string if ch.isdigit())
        dict_result['others'] = len(string) - dict_result['upper'] - dict_result['lower'] - dict_result['digits']
        dict_result['frequent_char'] = Counter(string).most_common(1)[0][0]
        return dict_result