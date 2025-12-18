"""
QUESTION:
Create a function `remove_duplicates_and_sort` that takes an array of integers as input. The function should remove all duplicate elements from the array, sort the remaining elements in descending order using a custom sorting algorithm (without using built-in sorting functions), and return the sorted array of unique elements.
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