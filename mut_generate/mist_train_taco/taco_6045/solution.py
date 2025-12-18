"""
QUESTION:
Some numbers can be expressed as a difference of two squares, for example, 20 = 6^(2)-4^(2) and 21 = 5^(2)-2^(2). Many numbers can be written this way, but not all.

## Your Task
Complete the function that takes a positive integer `n` and returns the amount of numbers between `1` and `n` (inclusive) that can be represented as the difference of two perfect squares.

**Note**: Your code should be able to handle `n` values up to 45000

## Examples

```
n = 4 ==> 3
n = 5 ==> 4
n = 10 ==> 7
n = 20 ==> 15
n = 6427 ==> 4820
```
"""

def count_squareable_numbers(n: int) -> int:
    """
    Counts the number of integers between 1 and n (inclusive) that can be expressed as the difference of two perfect squares.

    Parameters:
    n (int): A positive integer representing the upper limit of the range (inclusive).

    Returns:
    int: The count of numbers between 1 and n that can be expressed as the difference of two perfect squares.
    """
    return n // 4 + (n + 1) // 2