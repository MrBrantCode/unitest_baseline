"""
QUESTION:
Create a function called `identify_numbers` that takes a list of positive integers as input and returns a dictionary with two keys: 'perfect_squares' and 'perfect_cubes'. The function should identify which numbers in the input list are perfect squares and perfect cubes, and store them in their respective lists in the output dictionary.
"""

def identify_numbers(numbers):
    result = {'perfect_squares': [], 'perfect_cubes': []}
    for num in numbers:
        square_root = num ** 0.5
        cube_root = num ** (1./3.)
        
        # Check for perfect square
        if round(square_root) ** 2 == num:
            result['perfect_squares'].append(num)
        
        # Check for perfect cube
        if round(cube_root) ** 3 == num:
            result['perfect_cubes'].append(num)
    
    return result