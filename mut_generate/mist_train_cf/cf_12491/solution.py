"""
QUESTION:
Implement the `find_max` function to find the maximum value in an array of integers and count the number of comparisons made during the search. The function should return a tuple containing the maximum value and the total number of comparisons. The input array may be empty, and the function should handle this case by returning `None` as the maximum value and `0` as the number of comparisons.
"""

def find_max(arr):
    if len(arr) == 0:
        return None, 0

    max_value = arr[0]
    comparisons = 0

    for i in range(1, len(arr)):
        comparisons += 1
        if arr[i] > max_value:
            max_value = arr[i]

    return max_value, comparisons