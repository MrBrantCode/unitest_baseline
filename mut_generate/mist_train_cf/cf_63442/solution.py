"""
QUESTION:
Given a rectangular grid of wells where 1 represents a unit of water and 0 represents no water, and a bucket of fixed capacity, write a function named `well_emptying` that takes the grid and capacity as parameters and returns the number of bucket lowerings required to empty all the wells. The function should assume that all buckets have the same capacity and should work for grids with varying sizes.
"""

def well_emptying(grid, capacity):
    # Get the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])

    # Initialize the number of bucket lowerings to 0
    lowerings = 0

    # Iterate over the rows in the grid
    for i in range(rows):
        # Initialize the remaining capacity of the bucket
        remaining_capacity = capacity

        # Iterate over the columns in the row
        for j in range(cols):
            # If the current well has water
            if grid[i][j] == 1:
                # Decrease the remaining capacity of the bucket
                remaining_capacity -= 1

                # If the bucket is full, empty it and reset the capacity
                if remaining_capacity == 0:
                    lowerings += 1
                    remaining_capacity = capacity

        # If the bucket has water after finishing a row, empty it
        if remaining_capacity != capacity:
            lowerings += 1

    return lowerings