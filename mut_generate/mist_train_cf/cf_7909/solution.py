"""
QUESTION:
Write a function `unique_values` that takes an array of integers as input and returns a list of tuples, where each tuple contains a unique value from the array and its frequency of occurrence. The returned list should be sorted in ascending order based on the frequency of occurrence. The function should have a time complexity of O(n), where n is the length of the input array, and should not use any built-in Python functions for counting frequencies or sorting. Implement your own algorithms for counting and sorting.
"""

def unique_values(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1])
    return sorted_frequency