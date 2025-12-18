"""
QUESTION:
Given a name, turn that name into a perfect square matrix (nested array with the amount of arrays equivalent to the length of each array). 

You will need to add periods (`.`) to the end of the name if necessary, to turn it into a matrix. 

If the name has a length of 0, return `"name must be at least one letter"`

## Examples

"Bill" ==> [ ["B", "i"],
             ["l", "l"] ]

"Frank" ==> [ ["F", "r", "a"],
              ["n", "k", "."],
              [".", ".", "."] ]
"""

from math import ceil

def convert_name_to_square_matrix(name: str) -> list[list[str]] | str:
    if not name:
        return "name must be at least one letter"
    
    # Calculate the size of the square matrix
    matrix_size = ceil(len(name) ** 0.5)
    
    # Pad the name with periods to make its length a perfect square
    padded_name = name.ljust(matrix_size * matrix_size, '.')
    
    # Create the matrix
    matrix = [
        [padded_name[i * matrix_size + j] for j in range(matrix_size)]
        for i in range(matrix_size)
    ]
    
    return matrix