"""
QUESTION:
Write a function named `longest_zero_sequence` that takes a string of binary digits as input and returns the index of the first zero in the longest consecutive sequence of zeros. If there are multiple sequences of the same length, return the index of the first occurring sequence. The function should handle binary strings of any length.
"""

def longest_zero_sequence(binary_string):
    max_zeros = -1
    start_index = -1
    current_zeros = -1
    current_start = -1
    
    for i, char in enumerate(binary_string):
        if char == '0':
            if current_zeros == -1:
                current_start = i
            current_zeros += 1
            
            if current_zeros > max_zeros:
                max_zeros = current_zeros
                start_index = current_start
        else:
            current_zeros = -1
    
    return start_index