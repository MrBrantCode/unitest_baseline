"""
QUESTION:
Write a function `count_tokens` that takes a string of programming language syntax as input and returns the frequency count of distinct words and symbols, as well as two boolean values indicating whether the input contains nested loops and conditional statements, respectively. The function should be able to tokenize the input string, detect loops and conditions by checking specific keywords, and return the results.
"""

import re
from collections import Counter

def count_tokens(text):
    # Tokenizing the input string using regex
    tokens = re.findall(r'\b\w+\b|[!@#%^&*().:;,<>/{}|?=\-\+\[\]"`~]', text)
    
    # Using Counter to count frequency of each distinct token
    frequency = Counter(tokens)
    
    # Detecting loops/conditions by checking specific keywords
    nested_loops = any(token in ['for', 'while'] for token in frequency.keys())
    conditions = any(token in ['if', 'else', 'elif', 'switch'] for token in frequency.keys())
    
    return frequency, nested_loops, conditions