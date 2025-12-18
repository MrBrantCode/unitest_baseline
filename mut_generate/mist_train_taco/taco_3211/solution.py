"""
QUESTION:
In this Kata, you will be given an array of integers and your task is to return the number of arithmetic progressions of size `3` that are possible from that list. In each progression, the differences between the elements must be the same.

```
[1, 2, 3, 5, 7, 9] ==> 5
// [1, 2, 3], [1, 3, 5], [1, 5, 9], [3, 5, 7], and [5, 7, 9]
```

All inputs will be sorted. More examples in test cases. 

Good luck!
"""

def count_arithmetic_progressions(arr):
    """
    Counts the number of arithmetic progressions of size 3 that can be formed from a sorted list of integers.

    Parameters:
    arr (list of int): A sorted list of integers.

    Returns:
    int: The number of arithmetic progressions of size 3.
    """
    return sum((y - x == z - y for (i, x) in enumerate(arr[:-2]) for (j, y) in enumerate(arr[i + 1:-1]) for (_, z) in enumerate(arr[j + 1:])))