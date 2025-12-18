"""
QUESTION:
## Objective

Given a number `n` we will define it's sXORe to be `0 XOR 1 XOR 2 ... XOR n` where `XOR` is the [bitwise XOR operator](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

Write a function that takes `n` and returns it's sXORe.

## Examples
|    n    | sXORe n
|---------|--------         
| 0       | 0
| 1       | 1
| 50      | 51
| 1000000 | 1000000
---
"""

def calculate_sxore(n: int) -> int:
    """
    Calculate the sXORe of a given number n.

    The sXORe is defined as the result of the XOR operation applied to all integers from 0 to n.

    Parameters:
    n (int): The number for which to calculate the sXORe.

    Returns:
    int: The sXORe of the number n.
    """
    return [n, 1, n + 1, 0][n % 4]