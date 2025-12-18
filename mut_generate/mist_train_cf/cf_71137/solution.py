"""
QUESTION:
Write a function named `sum_evenid_within_bounds` that takes a list of integers and two integer parameters as input. The function should return `True` if the cumulative sum of all integers at even indices in the list is within the range between the two parameters (inclusively), and `False` otherwise. The list must have an even number of non-empty elements.
"""

def sum_evenid_within_bounds(l: list, lower_limit: int, upper_limit: int):
    # check the conditions for the array
    if len(l) % 2 != 0 or len(l) == 0:
        return False

    # calculate the sum of the elements at even indices
    sum_evenid = sum(l[i] for i in range(0, len(l), 2))

    # return True if the sum is within the limits, otherwise return False
    return lower_limit <= sum_evenid <= upper_limit