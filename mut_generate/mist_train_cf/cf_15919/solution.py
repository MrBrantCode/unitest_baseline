"""
QUESTION:
Write a function named `sum_of_cubes` that takes a positive integer `n` as input and returns the sum of the cubes of each digit in `n`. The function should be able to handle any positive integer input.
"""

def sum_of_cubes(n):
    total_sum = 0
    # Convert the number to a string to iterate over its digits
    n_str = str(n)
    
    # Iterate over each digit in the number
    for digit in n_str:
        # Convert the digit back to an integer and cube it
        digit_cube = int(digit) ** 3
        # Add the cube to the total sum
        total_sum += digit_cube
    
    return total_sum