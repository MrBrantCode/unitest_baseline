"""
QUESTION:
Write a function named `refresh_gradient` that generates a 10x10 grid filled with squares of different colors, following a gradient pattern. The gradient should transition from blue at the top left corner to green at the bottom right corner. The function should also allow for a change in gradient orientation between horizontal and vertical. The function should use a color model where the red channel remains constant at 0, and the blue and green channels vary according to the row and column indexes.
"""

def refresh_gradient(direction, width=10, height=10):
    image = [[(0, int((y/height)*255), int((x/width)*255)) if direction == "normal" else (0, int((y/height)*255), int((x/width)*255)) for x in range(width)] for y in range(height)]
    return image