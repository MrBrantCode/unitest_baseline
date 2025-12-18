"""
QUESTION:
## Number pyramid

Number pyramid is a recursive structure where each next row is constructed by adding adjacent values of the current row. For example:

```
Row 1     [1     2     3     4]
Row 2        [3     5     7]
Row 3           [8    12]
Row 4             [20]
```

___

## Task

Given the first row of the number pyramid, find the value stored in its last row.

___

## Examples

```python
reduce_pyramid([1])        ==  1
reduce_pyramid([3, 5])     ==  8
reduce_pyramid([3, 9, 4])  ==  25
```

___

## Performance tests

```python
Number of tests: 10
List size: 10,000
```
"""

def reduce_pyramid(base):
    def comb_n(n):
        c = 1
        for k in range(0, n + 1):
            yield c
            c = c * (n - k) // (k + 1)
    
    from operator import mul
    return sum(map(mul, base, comb_n(len(base) - 1)))