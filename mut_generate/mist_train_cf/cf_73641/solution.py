"""
QUESTION:
Write a function `analyze_string` that takes a string `input_string` as input and returns a list of tuples, where each tuple contains an alphanumeric character and its frequency in the string, ignoring case and special characters. The list should be sorted by frequency in descending order and then alphabetically.
"""

from collections import Counter

def analyze_string(input_string):
    # convert to lowercase and replace special characters
    input_string = ''.join(e for e in input_string if e.isalnum()).lower()
    
    # count character frequency
    freq = Counter(input_string)
    
    # sort by frequency and then alphabetically
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    return sorted_freq