"""
QUESTION:
Write a function called `swap_pairs` that takes a string of digits and an integer `pair_count` as input. The function should swap pairs of `pair_count` length in the string, and return the resulting string. If the remaining characters at the end of the string are less than `pair_count`, they should be appended to the resulting string without modification.
"""

def swap_pairs(string, pair_count):
    pairs_swapped = ""
    str_len = len(string)
    
    # loop through string, incrementing by pair_count each time
    for i in range(0, str_len, 2*pair_count):
        current_pair = string[i:i+2*pair_count]
        # if pair is full, reverse it and add to new string
        if len(current_pair) == 2*pair_count:
            current_pair = current_pair[::-1]
        pairs_swapped += current_pair
        
    return pairs_swapped