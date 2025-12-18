"""
QUESTION:
Given a sequence of numbers, find the largest pair sum in the sequence.

For example
```
[10, 14, 2, 23, 19] -->  42 (= 23 + 19)
[99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
```

Input sequence contains minimum two elements and every element is an integer.
"""

def largest_pair_sum(numbers):
    """
    Find the largest pair sum in the given sequence of numbers.

    Parameters:
    numbers (list of int): A list of integers.

    Returns:
    int: The largest pair sum in the sequence.
    """
    return sum(sorted(numbers)[-2:])