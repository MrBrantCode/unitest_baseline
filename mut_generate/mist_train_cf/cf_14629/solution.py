"""
QUESTION:
Write a function `convert_pyramid(pyramid)` that takes a 2D list `pyramid` representing a pyramid of numbers as input and returns a single number, which is the sum of the maximum path from the top to the bottom of the pyramid. The function should not modify the original `pyramid` list.
"""

def convert_pyramid(pyramid):
    # Create a new list to store the modified pyramid
    new_pyramid = [row[:] for row in pyramid]

    for i in range(len(pyramid)-2, -1, -1):
        for j in range(i+1):
            new_pyramid[i][j] += max(new_pyramid[i+1][j], new_pyramid[i+1][j+1])
    return new_pyramid[0][0]