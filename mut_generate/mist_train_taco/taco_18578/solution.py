"""
QUESTION:
Complete the function that takes two integers (`a, b`, where `a < b`) and return an array of all integers between the input parameters, **including** them.

For example:
```
a = 1
b = 4
--> [1, 2, 3, 4]
```
"""

def generate_range(a: int, b: int) -> list[int]:
    """
    Generate a list of integers from `a` to `b` (inclusive).

    Parameters:
    - a (int): The starting integer (inclusive).
    - b (int): The ending integer (inclusive).

    Returns:
    - list[int]: A list of integers from `a` to `b` (inclusive).
    """
    return list(range(a, b + 1))