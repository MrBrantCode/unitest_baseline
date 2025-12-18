"""
QUESTION:
Create a function `custom_sort_descending` that takes a list of integers as input. The function should return a new list containing only the unique elements from the input list in descending order. Implement a custom sorting algorithm instead of using built-in sorting functions.
"""

def custom_sort_descending(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    
    unique_elements = []
    for i in range(len(arr)):
        if arr[i] not in unique_elements:
            unique_elements.append(arr[i])
    
    return unique_elements