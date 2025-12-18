"""
QUESTION:
Implement a function `find_sum` that calculates the sum of all elements in a given array. The function should use a constant amount of space and have a time complexity of O(n), where n is the number of elements in the array. The function should handle an empty array as a valid input, returning 0 in such cases.
"""

def find_sum(arr):
    if not arr:
        return 0
    
    total = arr[0]  # initialize total with the first element
    n = len(arr)
    
    for i in range(1, n):
        total += arr[i]  # add each element to the total
        
    return total