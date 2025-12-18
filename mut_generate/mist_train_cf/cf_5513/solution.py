"""
QUESTION:
Design a function named `reverse_array` that takes an array of length n as an argument and returns the input array with its elements in reverse order. The function should only use constant extra space and have a time complexity of O(n), without using any built-in functions or data structures such as arrays or lists.
"""

def reverse_array(arr):
    n = len(arr)
    
    # Iterate over half of the array
    for i in range(n // 2):
        # Swap the elements at positions i and n-i-1
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    
    return arr