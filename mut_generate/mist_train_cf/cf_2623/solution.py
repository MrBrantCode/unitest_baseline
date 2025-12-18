"""
QUESTION:
Create a function `printShape2` that takes four parameters: `num` (a positive integer), `shape` (a string of length at most 10), `color` (a string in the format '#RRGGBB'), and `size` (a positive integer less than or equal to 100). The function should validate the inputs, printing an error message and returning if any are invalid. If valid, it should print the shape `num` times with its color and size. The size parameter represents the longer side of the rectangle if the shape is a rectangle, and the radius of the circle if the shape is a circle.
"""

def printShape2(num, shape, color, size):
    if not isinstance(num, int) or num <= 0:
        print("Invalid input: num must be a positive integer")
        return
    if not isinstance(shape, str) or len(shape) > 10:
        print("Invalid input: shape must be a string with length at most 10")
        return
    if not isinstance(color, str) or not color.startswith("#") or len(color) != 7 or not all(c.isdigit() or c in "ABCDEF" for c in color[1:]):
        print("Invalid input: color must be a string in the format '#RRGGBB'")
        return
    if not isinstance(size, int) or size <= 0 or size > 100:
        print("Invalid input: size must be a positive integer less than or equal to 100")
        return
    
    for _ in range(num):
        print(f"Printing {shape} in color {color} and size {size}")