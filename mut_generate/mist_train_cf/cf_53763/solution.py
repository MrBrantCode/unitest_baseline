"""
QUESTION:
Design a method `generate_spiral` that generates a spiral matrix pattern. The method should accept four parameters: `n` (number of rows in the matrix), `m` (number of columns in the matrix), `val` (initial value for the spiral), and `incr` (increment value for each successive element in the spiral). The method should return an `n`x`m` matrix filled with values in a spiral pattern, starting at `val` and incrementing by `incr` at each step.
"""

def generate_spiral(n, m, val, incr):
    # Initialize matrix
    matrix = [[0] * m for _ in range(n)]
 
    # Define the boundaries
    left, right, top, bottom = 0, m - 1, 0, n - 1
 
    # Counter to keep track of current value
    counter = val
 
    while True:
        # Print top row
        for i in range(left, right + 1):
            matrix[top][i] = counter
            counter += incr
        top += 1
        if top > bottom or left > right:
            break
 
        # Print right column
        for i in range(top, bottom + 1):
            matrix[i][right] = counter
            counter += incr
        right -= 1
        if top > bottom or left > right:
            break
 
        # Print bottom row
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = counter
            counter += incr
        bottom -= 1
        if top > bottom or left > right:
            break
 
        # Print left column
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = counter
            counter += incr
        left += 1
        if top > bottom or left > right:
            break
            
    return matrix