"""
QUESTION:
Given a positive integer n, define A(n) as the sum of the areas of all rectangles R such that the vertices of R have integer coordinates with absolute value ≤ n and the center of the largest-area circle inside R is (√13,0). Write a function A(n) that calculates the value of A(n). The function should take one parameter n and return the calculated value.
"""

def entrance(n):
    n = n // 6
    return 24 * n * (n + 1) * (2*n + 1) // 3