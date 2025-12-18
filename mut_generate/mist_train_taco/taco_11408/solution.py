"""
QUESTION:
Complete the function that takes 3 numbers `x, y and k` (where `x ≤ y`), and returns the number of integers within the range `[x..y]` (both ends included) that are divisible by `k`.

More scientifically:  `{ i : x ≤ i ≤ y, i mod k = 0 }`


## Example

Given ```x = 6, y = 11, k = 2``` the function should return `3`, because there are three numbers divisible by `2` between `6` and `11`: `6, 8, 10`

- **Note**: The test cases are very large. You will need a O(log n) solution or better to pass. (A constant time solution is possible.)
"""

def count_divisibles_in_range(x: int, y: int, k: int) -> int:
    """
    Counts the number of integers within the range [x..y] (both ends included) that are divisible by k.

    Parameters:
    - x (int): The lower bound of the range (inclusive).
    - y (int): The upper bound of the range (inclusive).
    - k (int): The divisor to check for divisibility.

    Returns:
    - int: The number of integers in the range [x..y] that are divisible by k.
    """
    return y // k - (x - 1) // k