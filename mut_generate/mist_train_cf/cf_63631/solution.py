"""
QUESTION:
The function `min_operations(s)` should take a string `s` consisting of lowercase English alphabets as input and return the minimum number of operations required to reproduce the string using a printer that can only print a continuous sequence of identical characters. The string length will not exceed 100 characters.
"""

def min_operations(s): 
    operations = 0
    current_char = ''
    
    for char in s:
        if char != current_char:
            operations += 1
            current_char = char
            
    return operations