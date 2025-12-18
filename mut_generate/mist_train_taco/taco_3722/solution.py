"""
QUESTION:
Find the length between 2 co-ordinates.  The co-ordinates are made of integers between -20 and 20 and will be given in the form of a 2D array:

(0,0) and (5,-7) would be [ [ 0 , 0 ] , [ 5, -7 ] ]

The function must return the answer rounded to 2 decimal places in the form of a string.

```python
length_of_line([[0, 0], [5, -7]]) => "8.60"
```

If the 2 given co-ordinates are the same, the returned length should be "0.00"
"""

from math import sqrt

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    if (x1, y1) == (x2, y2):
        return "0.00"
    
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return '{:.2f}'.format(distance)