"""
QUESTION:
Create a function `printShape2` that takes four parameters: an integer `num`, a string `shape`, a string `color` representing a color in the format '#RRGGBB', and a positive integer `size`. The function should validate the inputs, handle invalid inputs, and print the specified shape `num` times with its color and size. If the shape is a rectangle, `size` represents the length of the longer side; if the shape is a circle, `size` represents the radius. The function should output a string in the format "Printing [shape] in color [color] and size [size]" for each print.
"""

def printShape2(num, shape, color, size):
    if not isinstance(num, int) or num <= 0:
        print("Invalid number of times to print")
        return

    if not isinstance(shape, str):
        print("Invalid shape")
        return

    if not isinstance(color, str) or not color.startswith("#") or len(color) != 7:
        print("Invalid color")
        return

    if not isinstance(size, int) or size <= 0:
        print("Invalid size")
        return

    for i in range(num):
        print(f"Printing {shape} in color {color} and size {size}")