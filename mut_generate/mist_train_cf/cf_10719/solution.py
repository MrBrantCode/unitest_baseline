"""
QUESTION:
Write a function named `printShape(num, shape, color, size)` that prints a specified shape a certain number of times in a specified color and size. The function should validate its inputs and handle any invalid inputs appropriately. The function should take four parameters: `num` (the number of times to print the shape), `shape` (a single character string representing the shape to print), `color` (a string in the format '#RRGGBB' representing the color to print in), and `size` (a positive integer representing the size of the shape to print).
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