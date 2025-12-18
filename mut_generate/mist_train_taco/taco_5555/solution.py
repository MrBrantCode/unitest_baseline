"""
QUESTION:
# Task
A cake is sliced with `n` straight lines. Your task is to calculate the maximum number of pieces the cake can have.

# Example

 For `n = 0`, the output should be `1`.
 
 For `n = 1`, the output should be `2`.
 
 For `n = 2`, the output should be `4`.
 
 For `n = 3`, the output should be `7`.
 
 See the following image to understand it:
 
 ![](https://cdn2.scratch.mit.edu/get_image/project/92275349_500x400.png?v=1450672809.79)

# Input/Output


 - `[input]` integer `n`

  `0 ≤ n ≤ 10000`


 - `[output]` an integer

  The maximum number of pieces the sliced cake can have.
"""

def max_cake_pieces(n: int) -> int:
    """
    Calculate the maximum number of pieces a cake can have when sliced with `n` straight lines.

    Parameters:
    n (int): The number of straight lines used to slice the cake.

    Returns:
    int: The maximum number of pieces the cake can have.
    """
    return (n ** 2 + n + 2) // 2