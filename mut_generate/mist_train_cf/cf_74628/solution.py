"""
QUESTION:
Write a function `sublist_sums(lst)` that finds the sum of the largest and smallest sublists within a list of lists `lst` and returns their corresponding indices. If there are multiple sublists with the same largest or smallest sum, return the index of the first one. The function should handle negative numbers and empty sublists. The function should return a tuple containing two tuples, the first tuple containing the sum of the largest sublist and its index, and the second tuple containing the sum of the smallest sublist and its index.
"""

def sublist_sums(lst):
    max_sum = float('-inf')
    max_sum_index = None
    min_sum = float('inf')
    min_sum_index = None

    for index, sublist in enumerate(lst):
        sublist_sum = sum(sublist)
        if sublist_sum > max_sum:
            max_sum = sublist_sum
            max_sum_index = index
        if sublist_sum < min_sum:
            min_sum = sublist_sum
            min_sum_index = index

    return (max_sum, max_sum_index), (min_sum, min_sum_index)