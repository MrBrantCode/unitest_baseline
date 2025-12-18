"""
QUESTION:
Write a function `pascal_triangle(n)` that generates Pascal's Triangle up to the nth row. The function should print each row of the triangle and return True if `n` is greater than or equal to 1, and False otherwise. The function should only use a single loop and should handle cases where `n` is less than 1.
"""

def pascal_triangle(n):
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        print(trow)
        trow=[l+r for l,r in zip(trow+y, y+trow)]
    return n>=1