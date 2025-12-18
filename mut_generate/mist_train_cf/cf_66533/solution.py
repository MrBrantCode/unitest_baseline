"""
QUESTION:
Write a function `binary_search` to find the union of two sorted lists A and B without using built-in union functions. Implement a binary search technique to check for duplicate elements. The function should take two sorted lists A and B as input and return their union. The lists A and B are sorted in ascending order.
"""

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] > x:
            high = mid - 1
 
        else:
            return True
 
    return False

def union(A, B):
    result = A[:]
    for i in range(len(B)):
        if not binary_search(A, B[i]):
            result.append(B[i])
    return result