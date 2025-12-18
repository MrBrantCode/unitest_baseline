"""
QUESTION:
Write a function `compare_lists(list1, list2)` that takes two lists of equal length as input. The function should return a new list of equal length where each element corresponds to a comparison of the elements with the same index from the original lists. The comparison should be based on a ternary system: 0 if the elements are equal, -1 if the element from `list1` is less than the element from `list2`, and 1 if the element from `list1` is greater than the element from `list2`. The function should handle cases where elements in the input lists are non-numerical values, in which case it should append 'Invalid comparison' to the result list. The input lists may contain both integer and floating point numbers.
"""

def compare_lists(list1, list2):
    result = []

    for a, b in zip(list1, list2):
        try:
            # Perform numeric comparison
            if a == b:
                result.append(0)
            elif a < b:
                result.append(-1)
            else:
                result.append(1)
        except TypeError:
            # Handle case where comparison isn't possible
            result.append('Invalid comparison')

    return result