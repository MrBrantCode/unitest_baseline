"""
QUESTION:
Implement the function `replaceWithGreatest` that takes a 2D array as input and returns a new 2D array where every element is replaced with the greatest element in its row. The input array will have at most 10 rows and 10 columns, and all elements will be non-negative integers less than or equal to 100. The solution must utilize dynamic programming.
"""

def replaceWithGreatest(arr):
    rows = len(arr)
    cols = len(arr[0])
    
    # Create a new 2D array to store the modified array
    modified_arr = [[0] * cols for _ in range(rows)]
    
    # Iterate through each row of the array
    for i in range(rows):
        # Find the maximum element in the current row
        max_element = max(arr[i])
        
        # Replace each element in the row with the maximum element
        for j in range(cols):
            modified_arr[i][j] = max_element
    
    return modified_arr