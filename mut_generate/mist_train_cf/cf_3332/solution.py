"""
QUESTION:
Create a function named `remove_duplicates_and_sort` that takes an array as input and returns a new array with the following requirements: 
1. The array should contain only unique elements.
2. The array should be sorted in descending order.
3. The function should implement a custom sorting algorithm instead of using built-in sorting functions.
"""

def remove_duplicates_and_sort(arr):
    # Remove duplicates by converting the list to a set and back to a list
    unique_arr = list(set(arr))
    
    # Implement custom sorting algorithm in descending order
    n = len(unique_arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if unique_arr[j] < unique_arr[j + 1]:
                unique_arr[j], unique_arr[j + 1] = unique_arr[j + 1], unique_arr[j]
    
    return unique_arr