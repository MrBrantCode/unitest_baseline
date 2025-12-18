"""
QUESTION:
Write a function called `sum_of_odd_elements` that calculates the sum of all odd elements in a given matrix without using extra space. The function must iterate over the matrix only once. The matrix can have at least one row and one column and may include negative numbers.
"""

def sum_of_odd_elements(matrix):
    # Initialize sum variable
    sum = 0

    # Iterate over each row
    for row in matrix:
        # Iterate over each element in the row
        for num in row:
            # Check if element is odd
            if num % 2 != 0:
                # Add odd element to sum
                sum += num
    
    # Return sum
    return sum