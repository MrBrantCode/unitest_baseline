"""
QUESTION:
Complete the function that takes a non-negative integer `n` as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to `n` (inclusive).

## Examples

```python
n = 0  ==> [1]        # [2^0]
n = 1  ==> [1, 2]     # [2^0, 2^1]
n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]
```
"""

def generate_powers_of_two(n: int) -> list[int]:
    """
    Generates a list of all the powers of 2 with the exponent ranging from 0 to n (inclusive).

    :param n: A non-negative integer representing the highest exponent of 2.
    :return: A list of integers representing the powers of 2 from 2^0 to 2^n inclusive.
    """
    return [2 ** x for x in range(n + 1)]