"""
QUESTION:
Implement a function named `print_pascals_triangle` that takes an integer `num_rows` as input and prints a Pascal's triangle with the specified number of rows. The function should ensure that `num_rows` is a positive integer less than or equal to 10, and each number in the triangle should be the sum of the two numbers directly above it.
"""

def print_pascals_triangle(num_rows):
    # Validate the input
    if not isinstance(num_rows, int) or num_rows <= 0 or num_rows > 10:
        print("Number of rows should be a positive integer less than or equal to 10.")
        return
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Generate the remaining rows of the triangle
    for i in range(1, num_rows):
        previous_row = triangle[i - 1]
        current_row = [1]
        
        # Calculate each number in the current row
        for j in range(1, i):
            current_row.append(previous_row[j - 1] + previous_row[j])
            
        current_row.append(1)
        triangle.append(current_row)
    
    # Print the triangle
    for row in triangle:
        print(' '.join(map(str, row)).center(num_rows * 2))