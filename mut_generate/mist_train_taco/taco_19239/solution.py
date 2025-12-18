"""
QUESTION:
In this kata you will be given a sequence of the dimensions of rectangles ( sequence with width and length ) and circles ( radius - just a number ).  
Your task is to return a new sequence of dimensions, sorted ascending by area.

For example,

```python
seq = [ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ] # [ rectangle, circle, circle, rectangle ]
sort_by_area(seq) => [ ( 1.342, 3.212 ), 1.23, ( 4.23, 6.43 ), 3.444 ]
```

This kata inspired by [Sort rectangles and circles by area](https://www.codewars.com/kata/sort-rectangles-and-circles-by-area/).
"""

def sort_by_area(seq):
    def area(x):
        if isinstance(x, tuple):
            return x[0] * x[1]  # Area of a rectangle
        else:
            return 3.14 * x * x  # Area of a circle
    
    return sorted(seq, key=area)