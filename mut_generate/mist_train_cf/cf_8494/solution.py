"""
QUESTION:
Write a function `sum_special(arr)` that calculates the sum of all elements at even indices and the sum of all elements at odd indices in the given array `arr`. Implement the function to have a time complexity of O(n) and use a single loop to iterate through the array.
"""

def entrance(arr):
    even_sum = 0
    odd_sum = 0
    
    for i in range(0, len(arr), 2):
        even_sum += arr[i]
        if i + 1 < len(arr):
            odd_sum += arr[i + 1]
    
    return even_sum, odd_sum