"""
QUESTION:
Implement the function `find_maximum_sum` which calculates the maximum sum of elements in an array under the constraint that the elements used for summing must not be adjacent and have no common divisor more than 1. The function should handle arrays with at least two elements and integers within the array. Use the helper functions `pairwise_coprime` and `no_adjacent_elements` to verify the constraints. 

The `pairwise_coprime` function takes an array and start and end indexes as input and returns True if all pairs of numbers in the subarray have no common divisor more than 1, and False otherwise.

The `no_adjacent_elements` function takes an array and start and end indexes as input and returns True if there are no adjacent elements present between the start and end index in the array, and False otherwise.

The `find_maximum_sum` function should return the maximum possible sum of a subarray that satisfies the constraints.
"""

def find_maximum_sum(arr):
    n = len(arr)
    incl = arr[0]
    excl = 0

    for i in range(1, n):
        incl_new = excl + arr[i]
        excl_new = max(excl, incl)

        # Updating variables
        incl = incl_new
        excl = excl_new

    return max(excl, incl)