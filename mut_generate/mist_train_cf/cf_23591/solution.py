"""
QUESTION:
Write a function named `kthSmallest` that finds the kth smallest element in an array of integers. The function should take two parameters: `arr` (the input array) and `k` (the position of the element to find, where 1-indexing is used).
"""

def kthSmallest(arr, k): 
    arr.sort() 
    return arr[k-1]