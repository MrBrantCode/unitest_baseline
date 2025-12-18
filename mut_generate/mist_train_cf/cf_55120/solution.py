"""
QUESTION:
Write a function named `find_odd_occurrence` that accepts a list of integers and returns a list of integers. The returned list should contain the integers from the original list that appear an odd number of times.
"""

def find_odd_occurrence(lst):
    counter_dict = {}

    # Count frequency of each number in the list
    for num in lst:
        if num in counter_dict:
            counter_dict[num] += 1
        else:
            counter_dict[num] = 1

    # Filter out those that count only once
    odd_occurrence_list = [num for num, freq in counter_dict.items() if freq % 2 == 1]

    return odd_occurrence_list