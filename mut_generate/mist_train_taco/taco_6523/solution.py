"""
QUESTION:
Count the number of divisors of a positive integer `n`.

Random tests go up to `n = 500000`.

## Examples
```python
divisors(4)  == 3  # 1, 2, 4
divisors(5)  == 2  # 1, 5
divisors(12) == 6  # 1, 2, 3, 4, 6, 12
divisors(30) == 8  # 1, 2, 3, 5, 6, 10, 15, 30
```
"""

def count_divisors(n: int) -> int:
    """
    Count the number of divisors of a positive integer `n`.

    Parameters:
    n (int): The positive integer for which to count the divisors.

    Returns:
    int: The number of divisors of `n`.
    """
    return len([l_div for l_div in range(1, n + 1) if n % l_div == 0])