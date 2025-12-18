"""
QUESTION:
Implement a function named `unique_sorted_array` that takes an array of integers as input, removes duplicates, and returns the unique elements sorted in ascending order. The input array can be of any length and may contain negative numbers. The implementation must not use built-in sorting or duplicate removal functions or methods.
"""

def unique_sorted_array(arr):
    unique_elements = []
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)

    n = len(unique_elements)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if unique_elements[j] > unique_elements[j+1]:
                unique_elements[j], unique_elements[j+1] = unique_elements[j+1], unique_elements[j]

    return unique_elements