"""
QUESTION:
Complete the function ```circleArea``` so that it will return the area of a circle with the given ```radius```. Round the returned number to two decimal places (except for Haskell). If the radius is not positive or not a number, return ```false```.

Example:

```python
circleArea(-1485.86)     #returns false
circleArea(0)            #returns false
circleArea(43.2673)      #returns 5881.25
circleArea(68)           #returns 14526.72
circleArea("number")     #returns false
```
"""

from math import pi

def calculate_circle_area(radius):
    if isinstance(radius, (int, float)) and radius > 0:
        return round(pi * radius ** 2, 2)
    else:
        return False