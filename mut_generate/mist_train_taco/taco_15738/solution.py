"""
QUESTION:
```if-not:julia,racket
Write a function that returns the total surface area and volume of a box as an array: `[area, volume]`
```
```if:julia
Write a function that returns the total surface area and volume of a box as a tuple: `(area, volume)`
```
```if:racket
Write a function that returns the total surface area and volume of a box as a list: `'(area, volume)`
```
"""

def calculate_box_properties(w, h, d):
    area = 2 * (w * h + h * d + w * d)
    volume = w * h * d
    return [area, volume]