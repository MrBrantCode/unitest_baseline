"""
QUESTION:
Write a function `longest_contiguous_subarray` that takes an array of integers A and returns the length of the longest contiguous subarray where all elements are the same.
"""

def longest_contiguous_subarray(A):
    max_length = 1  
    start = 0  
    while start < len(A):
        end = start  
        while end < len(A) and A[start] == A[end]:  
            end += 1
        max_length = max(max_length, end - start)  
        start = end  
    return max_length