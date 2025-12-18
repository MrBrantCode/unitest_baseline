"""
QUESTION:
Write a Python function `replace_numbers(s)` that takes a string `s` as input and returns a new string where all digits in `s` are replaced with their corresponding word representations (e.g., '1' becomes 'one', '2' becomes 'two', etc.). The function should preserve non-digit characters in the original string.
"""

def replace_numbers(s):
    map_num_to_word = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', 
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    
    return ''.join(map_num_to_word[i] if i.isdigit() else i for i in s)