"""
QUESTION:
Given a number `n` we will define its scORe to be `0 | 1 | 2 | 3 | ... | n`, where `|` is the [bitwise OR operator](https://en.wikipedia.org/wiki/Bitwise_operation#OR).

Write a function that takes `n` and finds its scORe.

---------------------
|    n    | scORe n |
|---------|-------- |       
| 0       | 0 |
| 1       | 1 |
| 49      | 63 |
| 1000000 | 1048575 |
"""

def calculate_score(n: int) -> int:
    """
    Calculate the scORe of a given number `n` using the bitwise OR operator.

    The scORe of `n` is defined as `0 | 1 | 2 | 3 | ... | n`, where `|` is the bitwise OR operator.

    Parameters:
    n (int): The input number.

    Returns:
    int: The scORe of the input number `n`.
    """
    return 2 ** n.bit_length() - 1