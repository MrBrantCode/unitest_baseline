"""
QUESTION:
Write a function named `replace_with_sum` that takes an array as input, and modifies it to replace each element with the sum of all elements before it. The function must use a single loop, have a time complexity of O(n), where n is the length of the input array, and not use any additional arrays or data structures.
"""

def replace_with_sum(arr):
    if len(arr) == 0:
        return arr
    
    total_sum = arr[0]
    for i in range(1, len(arr)):
        arr[i], total_sum = total_sum, total_sum + arr[i]
    
    return arr