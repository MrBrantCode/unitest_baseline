"""
QUESTION:
Write a function named `min_max_sum` that takes a 2D array as input. The function should double each item in the array, sum the items from each row, and return the maximum and minimum sum of the rows. The solution should optimize for time complexity to work efficiently with large inputs.
"""

def min_max_sum(arr):
    min_sum = float('inf')
    max_sum = float('-inf')
    
    for row in arr:
        row_sum = sum(row) * 2
        
        if row_sum > max_sum:
            max_sum = row_sum
        
        if row_sum < min_sum:
            min_sum = row_sum
            
    return max_sum, min_sum