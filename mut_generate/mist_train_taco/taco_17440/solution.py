"""
QUESTION:
Draw a rectangle which has a height of H cm and a width of W cm. Draw a 1-cm square by single '#'.

Constraints

* 1 ≤ H ≤ 300
* 1 ≤ W ≤ 300

Input

The input consists of multiple datasets. Each dataset consists of two integers H and W separated by a single space.

The input ends with two 0 (when both H and W are zero).

Output

For each dataset, print the rectangle made of H × W '#'.

Print a blank line after each dataset.

Example

Input

3 4
5 6
2 2
0 0


Output

####
####
####

######
######
######
######
######

##
##
"""

def draw_rectangle(H: int, W: int) -> list[str]:
    """
    Draw a rectangle with height H and width W using '#' characters.

    Parameters:
    - H (int): The height of the rectangle.
    - W (int): The width of the rectangle.

    Returns:
    - list[str]: A list of strings where each string represents a row of the rectangle.
    """
    if H == 0 or W == 0:
        return []
    
    rectangle = ['#' * W for _ in range(H)]
    return rectangle