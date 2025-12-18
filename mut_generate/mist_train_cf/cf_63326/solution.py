"""
QUESTION:
Create a function named `draw_diamond(width)` that prints a hollow diamond pattern with the specified width and calculates its area. The function should only accept odd numbers as the width. If the input width is even, it should print an error message and return without drawing the diamond. The area of the diamond should be calculated as `(width*width)/2`.
"""

def draw_diamond(width):
    if width % 2 == 0:
        print("Width must be odd number!")
        return
    for i in range(width):
        print(' ' * abs((width//2) - i) + '*' + ' ' * 2*(min(i, width-i-1)) + '*'*(abs((width//2) - i)!=width//2))
    print("Area of the diamond: ", (width**2)/2)