"""
QUESTION:
Implement the function S(p) to calculate the cumulative sum of the perimeters of all Heron envelopes that have a perimeter less than or equal to p, where a Heron envelope is a convex figure with integral sides and diagonals, composed of an isosceles triangle atop a rectangle, and the perpendicular height of the flap is less than the height of the rectangle. The function S(p) should take an integer p as input and return the cumulative sum of perimeters as output.
"""

from math import gcd, sqrt
from array import array

def calculate_cumulative_sum(p):
    s1 = [0]*(p+1)
    arr = array('L', [])
    for n in range(1, int(sqrt(p//2))+1):
        for m in range(n-1, 0 , -2):
            if gcd(n, m) != 1:
                continue
            a = n * n - m * m
            b = 2 * n * m
            if a < b:  
                a, b = b, a
            x = a + 2 * b
            if x > p:
                continue
            h = b
            x = a
            while True:
                arr.append(x)
                x += h
                h += b
                if x > p:
                    break
    arr = sorted(arr)
    x0 = 0
    for x in arr:
        for i in range(x0+1, x+1):
            s1[i] = s1[i-1]
        x0 = x
        s1[x] += x
    return s1[p]