"""
QUESTION:
Create a function `sum_of_cubes` that takes an integer as input and returns the sum of the cubes of its digits. The input will be a non-negative integer.
"""

def sum_of_cubes(num):
    # Convert the number to string
    num_str = str(num)
    
    # Initialize sum of cubes to 0
    sum_cubes = 0
    
    # Iterate through each digit in the number
    for digit in num_str:
        # Convert the digit back to integer and cube it
        cube = int(digit) ** 3
        
        # Add the cube to the sum
        sum_cubes += cube
    
    # Return the sum of cubes
    return sum_cubes