"""
QUESTION:
Given a list of weights and a target sum n, create a function find_subset(weights, n) that determines if there is a subset of the weights that have a sum equal to n. The function should return True if such a subset exists, and False otherwise. Assume the weights are non-negative integers and n is a non-negative integer. The function should have a time complexity of O(n_items * n), where n_items is the number of items in the 'weights' array.
"""

def find_subset(weights, n):
    n_items = len(weights)
    subset = [[False for i in range(n + 1)] for j in range(n_items + 1)]
    # Initialize the first column to True
    for i in range(n_items + 1):
        subset[i][0] = True
    # Fill up the subset table in bottom-up manner
    for i in range(1, n_items + 1):
        for j in range(1, n + 1):
            if j < weights[i - 1]:
                subset[i][j] = subset[i - 1][j]
            if j >= weights[i - 1]:
                subset[i][j] = (subset[i - 1][j] or subset[i - 1][j - weights[i - 1]])
    # if the last element in the subset equals to True then there's a subset that adds up to n
    return subset[n_items][n]