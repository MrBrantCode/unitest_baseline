"""
QUESTION:
Implement a function `get_sum_at_odd_index(nested_list)` that calculates the sum of all individual elements situated at odd indexes in a nested list of integers. The index count starts at 0. The function should be able to handle nested lists of unknown depth.
"""

def get_sum_at_odd_index(nested_list):
    def helper(sub_list, depth=0):
        total = 0
        for i, e in enumerate(sub_list):
            if isinstance(e, list):
                total += helper(e, depth+1)
            elif i % 2 != 0:
                total += e
        return total

    return helper(nested_list)