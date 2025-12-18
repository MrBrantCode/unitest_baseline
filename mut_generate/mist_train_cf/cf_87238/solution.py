"""
QUESTION:
Write a function `unique_sorted_array` that takes an array of integers as input and returns a new array containing only the unique elements of the input array, sorted in ascending order. The function must not use any built-in sorting or duplicate removal functions or methods.
"""

def unique_sorted_array(arr):
    unique_elements = []
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)
    
    # Sort the unique elements using bubble sort
    n = len(unique_elements)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if unique_elements[j] > unique_elements[j+1]:
                unique_elements[j], unique_elements[j+1] = unique_elements[j+1], unique_elements[j]
    
    return unique_elements