"""
QUESTION:
Write a function named `fibonacci_search` to implement the Fibonacci search algorithm. The function should take a sorted list of integers `arr` and a target integer `x` as input, and return the index of `x` in `arr` if it exists, otherwise return -1. The function should only work with lists whose lengths are Fibonacci numbers.
"""

def fibonacci_search(arr, x):
    """
    This function implements the Fibonacci search algorithm.
    
    Parameters:
    arr (list): A sorted list of integers.
    x (int): The target integer to be searched.
    
    Returns:
    int: The index of x in arr if it exists, otherwise -1.
    """
    
    # Initialize fibonacci numbers
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci
    
    # Find the smallest Fibonacci Number greater than or equal to the length of arr
    while fibM < len(arr):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
    
    # Marks the eliminated range from front
    offset = -1
    
    while fibM > 1:
        # Check if fibMMm2 is a valid location
        i = min(offset + fibMMm2, len(arr) - 1)
        
        # If x is greater than the value at index fibMMm2, cut the subarray array from offset to i
        if arr[i] < x:
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        
        # If x is greater than the value at index fibMMm2, cut the subarray after i+1
        elif arr[i] > x:
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        
        # element found return index
        else:
            return i
    
    # comparing the last element with x
    if fibMMm1 and offset < len(arr) and arr[offset + 1] == x:
        return offset + 1
    
    # element not found
    return -1