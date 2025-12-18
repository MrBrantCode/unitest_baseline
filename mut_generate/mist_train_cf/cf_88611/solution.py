"""
QUESTION:
Design a function `swap_numbers(a, b)` that swaps two given numbers `a` and `b` without using a temporary variable and achieves a time complexity of O(1). The function should be able to handle swapping multiple pairs of numbers efficiently without impacting the time complexity. 

Additionally, design another function `swap_array_elements(arr, index1, index2)` that swaps two elements in the given array `arr` at indices `index1` and `index2` without modifying the original array.
"""

def swap_numbers(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

def swap_array_elements(arr, index1, index2):
    arr[index1] = arr[index1] ^ arr[index2]
    arr[index2] = arr[index1] ^ arr[index2]
    arr[index1] = arr[index1] ^ arr[index2]