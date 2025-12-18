"""
QUESTION:
Create a function named `sum_even_numbers` that calculates the sum of all even numbers in a given array. If the array is empty, the function should return 0. If the array contains no even numbers, the function should return -1.
"""

def sum_even_numbers(arr):
    if len(arr) == 0:
        return 0
    
    even_sum = 0
    has_even_number = False
    
    for num in arr:
        if num % 2 == 0:
            even_sum += num
            has_even_number = True
    
    if not has_even_number:
        return -1
    
    return even_sum