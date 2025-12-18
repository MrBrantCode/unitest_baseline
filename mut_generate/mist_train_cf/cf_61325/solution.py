"""
QUESTION:
Create a function named `process_array` that takes a list of integers `arr` as input. The function should return a list of tuples, where each tuple contains the cumulative sum of every successive pair of numbers in `arr` and a boolean value indicating whether the absolute difference between the pair of numbers exceeds 1. The function should iterate over all pairs of consecutive numbers in `arr`.
"""

def process_array(arr):
    result = []
    for i in range(len(arr)-1):
        sum = arr[i] + arr[i+1]
        if abs(arr[i] - arr[i+1]) > 1:
            result.append((sum, True))  
        else:
            result.append((sum, False))  
    return result