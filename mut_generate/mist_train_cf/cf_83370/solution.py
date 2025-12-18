"""
QUESTION:
Write a function named `swap_pairs` that takes three parameters: a string of digits `num_str`, an integer `pair_count`, and an integer `max_limit`. The function should swap pairs of adjacent digits in `num_str` up to `pair_count` times, but only if the resulting number does not exceed `max_limit`. If swapping a pair would exceed `max_limit`, do not perform that swap. The function should return the resulting string after all swaps have been attempted.
"""

def swap_pairs(num_str, pair_count, max_limit):
    num_list = list(num_str)
    for _ in range(pair_count):
        for i in range(0, len(num_list) - 1, 2):
            # Temporarily swap
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
            # Check it does not exceed the max_limit
            if int(''.join(num_list)) > max_limit:
                # If it does, swap back
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
    return ''.join(num_list)