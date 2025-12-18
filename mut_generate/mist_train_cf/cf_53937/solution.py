"""
QUESTION:
Write a function named `second_largest` that takes an array of integers as input and returns the second largest unique element in the array. If the array contains less than 2 unique elements, the function should return "Error: Less than 2 unique elements". The function should not use any pre-built functions for sorting or handling arrays.
"""

def second_largest(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    unique_elements = []
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)
    
    if len(unique_elements) < 2:
        return "Error: Less than 2 unique elements"
    else:
        return unique_elements[1]