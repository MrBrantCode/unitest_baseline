"""
QUESTION:
Write a Python function named `find_subsets_equal` that takes a list of integers `num_list` and a desired sum `desired_sum` as input. The function should return a tuple containing two values: the total number of elements in `num_list` and the total number of subsets of elements in `num_list` whose sum is equal to `desired_sum`. The list can include both positive and negative integers.
"""

from itertools import chain, combinations

def find_subsets_equal(num_list, desired_sum):
    all_subsets = list(chain(*map(lambda x: combinations(num_list, x), range(0, len(num_list)+1))))
    total_number_of_elements = len(num_list)
    match_subsets = [s for s in all_subsets if sum(s) == desired_sum]
    total_number_of_match_subsets = len(match_subsets)
    
    return total_number_of_elements, total_number_of_match_subsets