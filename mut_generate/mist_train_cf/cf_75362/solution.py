"""
QUESTION:
Create a function named `remove_kth_element` that takes two parameters: an array `arr` and an integer `k`. The function should return a new array that is identical to the input array `arr`, except with the k'th element removed. The array index is zero-based.
"""

def remove_kth_element(arr, k):
    return arr[:k] + arr[k+1:]