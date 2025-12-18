"""
QUESTION:
Write a function `pyramid_to_num(pyramid)` that takes a pyramid of numbers represented as a 2D list, where each inner list represents a row in the pyramid, and returns a single integer. The conversion process involves interpreting each row of the pyramid from left to right as a base-10 number, and then the entire pyramid as a base-2 number where the least significant digit is at the top.
"""

def pyramid_to_num(pyramid):
    num = 0
    for i, line in enumerate(pyramid):
        row_num = int(''.join(line))
        num += row_num * 2 ** (len(pyramid) - i - 1)
    return num