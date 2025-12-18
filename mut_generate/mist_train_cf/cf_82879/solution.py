"""
QUESTION:
Create a function called `dist_frequency` that takes a list of integers as input and returns a list of lists, where each sublist contains an integer from the input list and its frequency as a floating-point percentage of the total. The output list should be sorted by frequency in descending order and then by numerical value in ascending order. The input list can include negative numbers and zeros.
"""

def dist_frequency(lst):
    total = len(lst)
    distribution = {}
    for num in lst:
        if num in distribution:
            distribution[num] += 1
        else:
            distribution[num] = 1
    distr_lst = [[k, v/total * 100] for k, v in distribution.items()]
    distr_lst.sort(key=lambda x: (-x[1], x[0]))
    return distr_lst