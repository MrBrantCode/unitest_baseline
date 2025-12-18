"""
QUESTION:
A [sequence or a series](http://world.mathigon.org/Sequences), in mathematics, is a string of objects, like numbers, that follow a particular pattern. The individual elements in a sequence are called terms. A simple example is `3, 6, 9, 12, 15, 18, 21, ...`, where the pattern is: _"add 3 to the previous term"_.

In this kata, we will be using a more complicated sequence:   `0, 1, 3, 6, 10, 15, 21, 28, ...`
This sequence is generated with the pattern: _"the nth term is the sum of numbers from 0 to n, inclusive"_.

```
[ 0,  1,    3,      6,   ...]
  0  0+1  0+1+2  0+1+2+3
```

## Your Task

Complete the function that takes an integer `n` and returns a list/array of length `abs(n) + 1` of the arithmetic series explained above. When`n < 0` return the sequence with negative terms.

## Examples 

```
 5  -->  [0,  1,  3,  6,  10,  15]
-5  -->  [0, -1, -3, -6, -10, -15]
 7  -->  [0,  1,  3,  6,  10,  15,  21,  28]
```
"""

def generate_arithmetic_series(n: int) -> list[int]:
    """
    Generates an arithmetic series based on the given integer `n`.
    
    The series is generated such that the nth term is the sum of numbers from 0 to n, inclusive.
    If `n` is negative, the terms of the series will be negative.
    
    Parameters:
    - n (int): The integer input that determines the length and sign of the series.
    
    Returns:
    - list[int]: A list of integers representing the arithmetic series.
    """
    return [(-1 if n < 0 else 1) * sum(range(i + 1)) for i in range(abs(n) + 1)]