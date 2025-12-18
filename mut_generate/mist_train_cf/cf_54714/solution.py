"""
QUESTION:
Design a function `max_k_sum` that calculates the sum of the k largest numbers in a given array. The function should take two arguments: `arr` (the input array) and `k` (the number of largest numbers to sum). The function should return the sum of the k largest numbers. The input array may contain any number of elements, and k will be a positive integer less than or equal to the length of the array.
"""

def max_k_sum(arr, k):
    # We sort the array in descending order.
    arr.sort(reverse = True)
    # Then, we take the first K elements of the sorted array.
    max_k_elements = arr[:k]
    # We sum these elements.
    aggregate = sum(max_k_elements)
    # The function returns the aggregate.
    return aggregate