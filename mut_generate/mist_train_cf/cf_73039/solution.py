"""
QUESTION:
Write a function named `sum_unique_elements` that calculates the sum of the first n elements in a given array while excluding any repeating elements. The function should take an array as input and return the sum of unique elements.
"""

def sum_unique_elements(arr):
    unique_elements = set()
    total_sum = 0
    for element in arr:
        if element not in unique_elements:
            unique_elements.add(element)
            total_sum += element
    return total_sum