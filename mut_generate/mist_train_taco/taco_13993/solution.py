"""
QUESTION:
Hello! Your are given x and y and 2D array size tuple (width, height) and you have to:
Calculate the according index in 1D space (zero-based). 
Do reverse operation.

Implement:
to_1D(x, y, size):
  --returns index in 1D space
to_2D(n, size)
  --returns x and y in 2D space

1D array: [0, 1, 2, 3, 4, 5, 6, 7, 8]
2D array: [[0 -> (0,0), 1 -> (1,0), 2 -> (2,0)], 
           [3 -> (0,1), 4 -> (1,1), 5 -> (2,1)], 
           [6 -> (0,2), 7 -> (1,2), 8 -> (2,2)]]


to_1D(0, 0, (3,3)) returns 0
to_1D(1, 1, (3,3)) returns 4
to_1D(2, 2, (3,3)) returns 8
to_2D(5, (3,3)) returns (2,1)
to_2D(3, (3,3)) returns (0,1)

Assume all input are valid:

1 < width  < 500; 
1 < height < 500
"""

def convert_2d_to_1d(x: int, y: int, size: tuple) -> int:
    """
    Converts 2D coordinates (x, y) to a 1D index based on the given size of the 2D array.

    Parameters:
    - x (int): The x-coordinate in the 2D space.
    - y (int): The y-coordinate in the 2D space.
    - size (tuple): A tuple representing the size of the 2D array (width, height).

    Returns:
    - int: The corresponding index in the 1D space.
    """
    width, height = size
    return y * width + x

def convert_1d_to_2d(index: int, size: tuple) -> tuple:
    """
    Converts a 1D index to 2D coordinates (x, y) based on the given size of the 2D array.

    Parameters:
    - index (int): The index in the 1D space.
    - size (tuple): A tuple representing the size of the 2D array (width, height).

    Returns:
    - tuple: A tuple representing the x and y coordinates in the 2D space (x, y).
    """
    width, height = size
    return (index % width, index // width)