"""
QUESTION:
Given a triangle of consecutive odd numbers:

```
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
```

find the triangle's row knowing its index (the rows are 1-indexed), e.g.:

```
odd_row(1)  ==  [1]
odd_row(2)  ==  [3, 5]
odd_row(3)  ==  [7, 9, 11]
```

**Note**: your code should be optimized to handle big inputs.

___

The idea for this kata was taken from this kata: [Sum of odd numbers](https://www.codewars.com/kata/sum-of-odd-numbers)
"""

def generate_odd_row(n: int) -> list[int]:
    """
    Generate the nth row of the triangle of consecutive odd numbers.

    Args:
        n (int): The 1-indexed row number of the triangle.

    Returns:
        list[int]: A list of integers representing the odd numbers in the specified row.
    """
    start = n * (n - 1) + 1
    end = n * (n + 1)
    return list(range(start, end, 2))