"""
QUESTION:
Write a function `findMaxValueOfEquation` that takes in a list of points `points` where `points[i] = [xi, yi]`, an integer `k`, and integers `a` and `b` as input, and returns the maximum value of the equation `f(yi) + f(yj) + |xi - xj|` where `f(x) = ax + b`, `|xi - xj| <= k`, and `1 <= i < j <= points.length`. The list of points is sorted by the x-values, and `xi` form a strictly increasing sequence. The constraints are `2 <= points.length <= 10^5`, `-10^8 <= points[i][0], points[i][1], a, b <= 10^8`, and `0 <= k <= 2 * 10^8`.
"""

from heapq import heappop, heappush

def findMaxValueOfEquation(points, k, a, b):
    """
    This function calculates the maximum value of the equation f(yi) + f(yj) + |xi - xj| 
    where f(x) = ax + b, |xi - xj| <= k, and 1 <= i < j <= points.length.

    Args:
        points (List[List[int]]): A list of points where points[i] = [xi, yi].
        k (int): The constraint for |xi - xj|.
        a (int): The coefficient of x in the function f(x) = ax + b.
        b (int): The constant in the function f(x) = ax + b.

    Returns:
        int: The maximum value of the equation.
    """
    pq = []
    res = float('-inf')
    for x, y in points:
        while pq and x - pq[0][1] > k:
            heappop(pq)
        if pq:
            res = max(res, pq[0][0] + a*y + x + b)
        heappush(pq, (a * y - x, x))
    return res