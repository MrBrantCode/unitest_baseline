"""
QUESTION:
Write a function `sum_of_cubes(n)` that takes a positive integer `n` as input and returns the sum of the cubes of its digits if the sum is divisible by 7. If the sum is not divisible by 7, return "Not divisible by 7".
"""

def sum_of_cubes(n):
    # Convert the integer to a string to access its individual digits
    n_str = str(n)
    
    # Initialize a variable to store the sum of cubes
    sum_of_cubes = 0
    
    # Iterate through each digit in the string representation of the number
    for digit in n_str:
        # Convert the digit back to integer and cube it
        cube = int(digit) ** 3
        # Add the cube to the sum_of_cubes variable
        sum_of_cubes += cube
    
    # Check if the sum of cubes is divisible by 7
    if sum_of_cubes % 7 == 0:
        # Return the sum of cubes if it is divisible by 7
        return sum_of_cubes
    else:
        # Return "Not divisible by 7" if the sum of cubes is not divisible by 7
        return "Not divisible by 7"