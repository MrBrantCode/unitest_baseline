"""
QUESTION:
Create a function named `sort_array` that takes an array of integers as input. The function should sort the array in descending order and return the sorted array. The input array consists of positive integers ranging from 1 to 1000. The function must have a time complexity of O(n) and a space complexity of O(1), and it should not use any built-in sorting functions or libraries.
"""

def sort_array(arr):
    max_value = 1000
    count = [0] * (max_value + 1)
    result = []
    
    for num in arr:
        count[num] += 1
    
    for i in range(max_value, -1, -1):
        if count[i] > 0:
            result.extend([i] * count[i])
    
    return result