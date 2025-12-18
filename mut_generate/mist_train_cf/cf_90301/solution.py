"""
QUESTION:
Write a function called `sort_array` that takes an array of integers as input and returns the sorted array in descending order. The array consists of positive integers ranging from 1 to 1000. The function should have a time complexity of O(n) and a space complexity of O(1), and it should not use any built-in sorting functions or libraries. Implement the function using a recursive approach.
"""

def count_sort(arr, n, count, result, max_value):
    if n < 0:
        for i in range(max_value, -1, -1):
            if count[i] > 0:
                result.extend([i] * count[i])
        return result
    
    count[arr[n]] += 1
    
    return count_sort(arr, n - 1, count, result, max_value)

def sort_array(arr):
    max_value = 1000
    count = [0] * (max_value + 1)
    return count_sort(arr, len(arr) - 1, count, [], max_value)