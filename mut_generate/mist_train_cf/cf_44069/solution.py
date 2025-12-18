"""
QUESTION:
Write a function named `find_max_min` that takes an array of integers as input and returns the maximum and minimum values in the array. The array size varies from 10 to 100, and the function should be able to handle dynamic changes in array size efficiently. The function should iterate over the array only once to achieve a computational complexity of O(n).
"""

def find_max_min(arr):
    max_value = arr[0] 
    min_value = arr[0] 
    
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
        elif arr[i] < min_value:
            min_value = arr[i]
            
    return max_value, min_value