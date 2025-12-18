"""
QUESTION:
Write a function called `calculate_sum_divisible(array, n)` that takes a 2D array and an integer `n` as inputs. The function should return the indices of the rows in the array where the sum of the elements in the row is divisible by `n`. The function should not use any built-in sum functions or external libraries. If no rows satisfy the condition, the function should return an empty list.
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