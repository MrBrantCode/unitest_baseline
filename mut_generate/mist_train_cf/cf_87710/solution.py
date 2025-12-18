"""
QUESTION:
Write a function named `find_longest_sequence` that takes a binary string as input and returns the index of the first zero in the longest consecutive sequence of zeros surrounded by ones. If there are multiple sequences of the same length, return the index of the first occurring sequence. The binary string will have a length of at most 10^6 characters.
"""

def find_longest_sequence(binary_string):
    start = -1
    max_start = -1
    max_length = 0
    
    for i in range(len(binary_string)):
        if binary_string[i] == '0':
            if start == -1:
                start = i
        elif start != -1:
            length = i - start
            if length > max_length:
                max_start = start
                max_length = length
            start = -1
    
    if start != -1:
        length = len(binary_string) - start
        if length > max_length:
            max_start = start
            max_length = length
    
    return max_start