"""
QUESTION:
Given a string with alphanumeric characters and special symbols, write a function `transform_string` that accomplishes the following tasks: 

Invert the case of every alphabet character, find the next even number if a numerical character is uneven and keep it as is if already even (treat the whole number instead of individual digits if a sequence of digits forms a number), duplicate every special symbol, and produce a frequency count of each altered character in the transformed string. The function should return the transformed string and the frequency count as a tuple.
"""

import re
from collections import Counter

def transform_string(string: str):
    transformed = []
    string_copy = string
    while string_copy:
        num_match = re.match('\d+', string_copy)
        if num_match:
            num_str = num_match.group()
            num = int(num_str)
            if num % 2 == 1:
                num += 1
            transformed.append(str(num))
            string_copy = string_copy[num_match.end():]
            
        elif string_copy[0].isalpha():
            transformed.append(string_copy[0].swapcase())
            string_copy = string_copy[1:]
            
        elif not string_copy[0].isalnum():
            transformed.append(2*string_copy[0])
            string_copy = string_copy[1:]
            
    transformed = ''.join(transformed)
    freq_count = Counter(transformed)
    
    return transformed, freq_count