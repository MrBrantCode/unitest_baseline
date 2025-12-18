"""
QUESTION:
Here you will create the classic [Pascal's triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle).
Your function will be passed the depth of the triangle and you code has to return the corresponding pascal triangle up to that depth.

The triangle should be returned as a nested array.

for example:
```python
pascal(5) # should return [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
```

To build the triangle, start with a single 1 at the top, for each number in the next row you just take the two numbers above it and add them together (except for the edges, which are all `1`), e.g.:
```
              [1]
            [1   1]
          [1   2   1]
        [1   3   3   1]
```
"""

def generate_pascals_triangle(depth: int) -> list[list[int]]:
    if depth <= 0:
        return []
    
    triangle = [[1]]
    for _ in range(depth - 1):
        to_sum = list(zip([0] + triangle[-1], triangle[-1] + [0]))
        triangle.append(list(map(sum, to_sum)))
    
    return triangle