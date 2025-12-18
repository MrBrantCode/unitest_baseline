"""
QUESTION:
Write a function `int_inversion` that takes a string of concatenated integers and a list of digit counts for each integer as input. The function should return a list of integers where each integer is a substring of the input string with a length corresponding to its digit count in the list. The input string is guaranteed to be a concatenation of non-negative integers. 

The input parameters are `concat_str` (a string of concatenated integers) and `digit_counts` (a list of digit counts for each integer). The function should not include any error handling or input validation.
"""

def int_inversion(concat_str, digit_counts):
    curr_index = 0
    int_list = []
    for count in digit_counts:
        int_chunk = int(concat_str[curr_index: curr_index + count])
        int_list.append(int_chunk)
        curr_index += count
    return int_list