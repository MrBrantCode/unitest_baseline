"""
QUESTION:
Write a function `generate_pascals_triangle` that generates Pascal's triangle up to a given row number `n`. The function should return the generated Pascal's triangle as a 2D list, the sum of all elements in the triangle, and the maximum element in each row. The row number `n` is a prime number and less than 100. The time complexity of the function should be O(n^2).
"""

import math

def generate_pascals_triangle(n):
    """
    Generates Pascal's triangle up to a given row number n.
    
    Args:
        n (int): The row number up to which the triangle should be generated.
        
    Returns:
        list: A 2D list representing Pascal's triangle.
        int: The sum of all elements in the triangle.
        list: A list of tuples containing the maximum element in each row and its row number.
    """
    
    pascals_triangle = []
    total_sum = 0
    max_elements = []
    
    for i in range(n):
        row = [1]
        
        if i > 0:
            previous_row = pascals_triangle[i-1]
            
            for j in range(len(previous_row) - 1):
                row.append(previous_row[j] + previous_row[j+1])
        
            row.append(1)
        
        pascals_triangle.append(row)
        total_sum += sum(row)
        max_elements.append((i+1, max(row)))
    
    return pascals_triangle, total_sum, max_elements