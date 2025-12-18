"""
QUESTION:
Implement a recursive function `count_elements` that takes an array of positive integers and two integers `k` and `m` as input, and returns the number of elements in the array that are divisible by `k` and have a remainder of 1 when divided by `m`.
"""

def count_elements(arr, k, m, index=0, count=0):
    if index == len(arr):
        return count
    
    if arr[index] % k == 0 and arr[index] % m == 1:
        count += 1
    
    return count_elements(arr, k, m, index+1, count)