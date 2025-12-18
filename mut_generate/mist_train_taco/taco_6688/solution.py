"""
QUESTION:
# Task
 The `hamming distance` between a pair of numbers is the number of binary bits that differ in their binary notation. 
 
# Example

 For `a = 25, b= 87`, the result should be `4`
```
25: 00011001
87: 01010111
```
The `hamming distance` between these two would be 4 ( the `2nd, 5th, 6th, 7th` bit ).


# Input/Output


 - `[input]` integer `a`

  First Number. `1 <= a <= 2^20`


 - `[input]` integer `b`

  Second Number. `1 <= b <= 2^20`


 - `[output]` an integer

  Hamming Distance
"""

def calculate_hamming_distance(a: int, b: int) -> int:
    """
    Calculate the Hamming distance between two integers.

    The Hamming distance is the number of differing bits in the binary representation of the two integers.

    Parameters:
    - a (int): The first integer.
    - b (int): The second integer.

    Returns:
    - int: The Hamming distance between the two integers.
    """
    return bin(a ^ b).count('1')