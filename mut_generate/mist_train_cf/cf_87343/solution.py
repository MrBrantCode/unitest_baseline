"""
QUESTION:
Write a function called `remove_duplicates` that takes an array of integers as input, removes duplicates, sorts the array in descending order, and returns the sorted array along with the sum of its elements. The function should include negative numbers in the sorted array.
"""

def remove_duplicates(arr):
    unique_array = []
    for num in arr:
        if num not in unique_array:
            unique_array.append(num)
    unique_array.sort(reverse=True)
    return unique_array, sum(unique_array)