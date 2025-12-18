"""
QUESTION:
Write a function `find_diagonals` that calculates the number of distinct diagonals in a convex polygon given the number of vertices `n`. The function should return the total count of distinct diagonals. The polygon is convex, meaning all diagonals lie inside the polygon.
"""

def find_diagonals(n):
    return n*(n-3)//2