"""
QUESTION:
Write the following function:

```python
def area_of_polygon_inside_circle(circle_radius, number_of_sides):
```

It should calculate the area of a regular polygon of `numberOfSides`, `number-of-sides`, or `number_of_sides` sides inside a circle of radius `circleRadius`, `circle-radius`, or `circle_radius` which passes through all the vertices of the polygon (such circle is called [**circumscribed circle** or **circumcircle**](https://en.wikipedia.org/wiki/Circumscribed_circle)). The answer should be a number rounded to 3 decimal places. 

Input :: Output Examples 

```python
area_of_polygon_inside_circle(3, 3) # returns 11.691

area_of_polygon_inside_circle(5.8, 7) # returns 92.053

area_of_polygon_inside_circle(4, 5) # returns 38.042
```
"""

from math import sin, pi

def area_of_polygon_inside_circle(circle_radius, number_of_sides):
    return round(0.5 * number_of_sides * circle_radius ** 2 * sin(2 * pi / number_of_sides), 3)