"""
QUESTION:
Given an array of integers and a number n, write a function `calculate_sum_divisible(array, n)` that returns a list of row indices where the sum of the elements in the row is divisible by n without using any built-in functions for sum or external libraries.
"""

def calculate_sum_divisible(array, n):
    divisible_indices = []
    
    for i in range(len(array)):
        row_sum = 0
        for j in range(len(array[i])):
            row_sum += array[i][j]
        
        if row_sum % n == 0:
            divisible_indices.append(i)
            
    return divisible_indices