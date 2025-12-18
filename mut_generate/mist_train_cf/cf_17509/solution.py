"""
QUESTION:
Create a function `printShape2` that takes four parameters: 
- `num`: an integer representing the number of times the shape should be printed.
- `shape`: a string representing the shape to be printed.
- `color`: a string representing the color of the shape in the format '#RRGGBB'.
- `size`: a positive integer representing the size of the shape, with 'size' representing the length of the longer side for rectangles and the radius for circles.
The function should validate the inputs and print the shape 'num' times, each time specifying the shape, color, and size, or provide an error message for invalid inputs.
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