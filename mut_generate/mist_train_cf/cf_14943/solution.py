"""
QUESTION:
Write a function `replace_with_sum` that takes an array `arr` as input and replaces each element with the sum of all elements before it. The function must use a single loop and not use any additional arrays or data structures. The time complexity of the function should be O(n), where n is the length of the input array.
"""

def replace_with_sum(arr):
    if len(arr) == 0:
        return arr
    
    total_sum = arr[0]
    for i in range(1, len(arr)):
        arr[i], total_sum = total_sum, total_sum + arr[i]
    
    return arr