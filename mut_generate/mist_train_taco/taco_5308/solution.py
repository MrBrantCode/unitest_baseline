"""
QUESTION:
# Task:

Based on the received dimensions, `a` and `b`, of an ellipse, calculare its area and perimeter.

## Example:
```python
Input: ellipse(5,2)

Output: "Area: 31.4, perimeter: 23.1"
```

**Note:** The perimeter approximation formula you should use: `π * (3/2(a+b) - sqrt(ab))`

___

## Have fun :)
"""

from math import pi, sqrt

def calculate_ellipse_properties(a, b):
    # Calculate the area of the ellipse
    area = pi * a * b
    
    # Calculate the perimeter of the ellipse using the given approximation formula
    perimeter = pi * (1.5 * (a + b) - sqrt(a * b))
    
    return area, perimeter