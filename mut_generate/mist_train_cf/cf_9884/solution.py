"""
QUESTION:
Create a function `print_triangle(height, symbol)` that prints a triangle of a specified symbol. The triangle should have a height of `height` rows, where `height` must be a positive integer between 1 and 10 (inclusive), and the symbol used for the triangle is specified by `symbol`, which can be any printable ASCII character. The triangle should be printed with each row containing one more symbol than the previous row, centered within the triangle.
"""

def print_triangle(height, symbol):
    if height < 1 or height > 10:
        print("Invalid height. Please enter a positive integer between 1 and 10.")
        return
    
    for i in range(height):
        row = (symbol * (2*i + 1)).center(2*height - 1)
        print(row)