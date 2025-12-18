"""
QUESTION:
# Task
 Given two cells on the standard chess board, determine whether they have the same color or not.

# Example

 For `cell1 = "A1" and cell2 = "C3"`, the output should be `true`.
 For `cell1 = "A1" and cell2 = "H3"`, the output should be `false`.

# Input/Output

 - `[input]` string `cell1`
 
 - `[input]` string `cell2`
 
 - `[output]` a boolean value

    `true` if both cells have the same color, `false` otherwise.
"""

def are_cells_same_color(cell1: str, cell2: str) -> bool:
    return (ord(cell1[0]) + int(cell1[1])) % 2 == (ord(cell2[0]) + int(cell2[1])) % 2