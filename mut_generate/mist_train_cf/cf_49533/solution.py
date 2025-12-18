"""
QUESTION:
You are given an array `rectangles` where `rectangles[i] = [li, wi, ci]` represents the `ith` rectangle of length `li`, width `wi`, and color `ci`. Write a function `countMaxLenRectangles(rectangles, color)` that returns the number of rectangles that can make a square with the maximum possible side length and the specific color `c`. The function should consider that you can cut the `ith` rectangle to form a square with a side length of `k` if both `k <= li` and `k <= wi`. The input `color` is the specific color for which you need to find the count of rectangles. 

Constraints:
`1 <= rectangles.length <= 1000`
`rectangles[i].length == 3`
`1 <= li, wi <= 10^9`
`li != wi`
`1 <= ci <= 10^9`
"""

from collections import defaultdict

def countMaxLenRectangles(rectangles, color):
    rectangles = [(min(l, w), c) for l, w, c in rectangles]
    rectangles.sort(reverse=True)

    best = 0
    count = defaultdict(int)
    for l, c in rectangles:
        if l < best:
            break
        if c == color:
            best = l
            count[c] += 1

    return count[color]