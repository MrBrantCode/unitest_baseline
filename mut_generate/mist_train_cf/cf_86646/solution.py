"""
QUESTION:
Create a function `sum_lists` that takes two lists of integers `a` and `b` as input, and returns a list containing the sum of each corresponding pair of integers from `a` and `b`. The function should have a time complexity of O(n), where n is the length of the input lists. Note that the input lists are of the same length.
"""

def sum_lists(a, b):
    # Create an empty list to store the sums
    result = []

    # Iterate through the lists a and b
    for i in range(len(a)):
        # Add the corresponding elements from a and b and append the sum to the result list
        result.append(a[i] + b[i])

    return result