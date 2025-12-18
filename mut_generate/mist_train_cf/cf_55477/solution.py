"""
QUESTION:
Create a function `generate_3d_array` that takes an integer `m` as input and returns a three-dimensional array of dimension `m x m x m`. The array should be populated with successive positive integers starting from 1 up to the cube of `m` in the order of depth-row-column (from back to front, top to bottom, left to right).
"""

def generate_3d_array(m):
    # Initialize an empty 3d array 
    three_d_array = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(m)]
    
    # Variable to hold the current number
    curr_num = 1

    # Populate the 3d array from back to front, top to bottom, left to right
    for depth in range(m):
        for row in range(m):
            for col in range(m):
                three_d_array[depth][row][col] = curr_num
                curr_num += 1
                
    return three_d_array