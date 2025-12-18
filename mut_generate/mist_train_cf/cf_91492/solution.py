"""
QUESTION:
Create a function named `printShape(num, shape, color, size)` that takes four parameters: the number of times to print the shape, the shape to be printed (a single character string), the color to print the shape in (a string in the format '#RRGGBB'), and the size of the shape (a positive integer). The function should validate its inputs and handle any invalid inputs by printing an error message.
"""

def printShape(num, shape, color, size):
    if not isinstance(num, int) or num <= 0:
        print("Error: num should be a positive integer")
        return
    if not isinstance(shape, str) or len(shape) != 1:
        print("Error: shape should be a single character string")
        return
    if not isinstance(color, str) or len(color) != 7 or color[0] != "#" or not all(c.isdigit() or c.lower() in "abcdef" for c in color[1:]):
        print("Error: color should be a string in the format '#RRGGBB'")
        return
    if not isinstance(size, int) or size <= 0:
        print("Error: size should be a positive integer")
        return

    for i in range(0, num):
        print(f"Printing {shape} in color {color} and size {size}")