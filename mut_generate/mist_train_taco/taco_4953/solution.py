"""
QUESTION:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
Task:
Write
```
smallest(n)
```
that will find the smallest positive number that is evenly divisible by all of the numbers from 1 to n (n <= 40). 
E.g
```python
smallest(5) == 60 # 1 to 5 can all divide evenly into 60
smallest(10) == 2520
```
"""

def smallest_divisible(n):
    """
    Finds the smallest positive number that is evenly divisible by all of the numbers from 1 to n.

    Parameters:
    n (int): The upper limit of the range (from 1 to n) for which we need to find the smallest divisible number.

    Returns:
    int: The smallest positive number that is evenly divisible by all numbers from 1 to n.
    """
    (x, y, m) = (1, 1, 1)
    while m <= n:
        if x % m == 0:
            m += 1
            y = int(x)
        else:
            x += y
    return x