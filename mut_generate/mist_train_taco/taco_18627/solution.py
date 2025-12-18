"""
QUESTION:
Given a non-negative integer, return an array / a list of the individual digits in order.

Examples:

```
123 => [1,2,3]

1 => [1]

8675309 => [8,6,7,5,3,0,9]
```
"""

def digitize(n: int) -> list[int]:
    """
    Converts a non-negative integer into a list of its individual digits in order.

    Parameters:
    n (int): The non-negative integer to be digitized.

    Returns:
    list[int]: A list of integers representing the individual digits of n.
    """
    return [int(d) for d in str(n)]