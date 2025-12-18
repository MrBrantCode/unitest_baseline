"""
QUESTION:
Your task is to make two functions, ```max``` and ```min``` (`maximum` and `minimum` in PHP and Python) that take a(n) array/vector of integers ```list``` as input and outputs, respectively, the largest and lowest number in that array/vector.

#Examples
```python
maximun([4,6,2,1,9,63,-134,566]) returns 566
minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
maximun([5]) returns 5
minimun([42, 54, 65, 87, 0]) returns 0
```

#Notes
- You may consider that there will not be any empty arrays/vectors.
"""

def find_maximum(numbers: list[int]) -> int:
    """
    Returns the largest integer in the given list of integers.

    :param numbers: A list of integers.
    :return: The largest integer in the list.
    """
    return max(numbers)

def find_minimum(numbers: list[int]) -> int:
    """
    Returns the smallest integer in the given list of integers.

    :param numbers: A list of integers.
    :return: The smallest integer in the list.
    """
    return min(numbers)