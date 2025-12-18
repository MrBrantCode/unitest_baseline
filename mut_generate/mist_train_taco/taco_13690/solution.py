"""
QUESTION:
You are given n points on a plane. All the points are distinct and no three of them lie on the same line. Find the number of parallelograms with the vertices at the given points.


-----Input-----

The first line of the input contains integer n (1 ≤ n ≤ 2000) — the number of points.

Each of the next n lines contains two integers (x_{i}, y_{i}) (0 ≤ x_{i}, y_{i} ≤ 10^9) — the coordinates of the i-th point.


-----Output-----

Print the only integer c — the number of parallelograms with the vertices at the given points.


-----Example-----
Input
4
0 1
1 0
1 1
2 0

Output
1
"""

from collections import Counter

def count_parallelograms(n, points):
    """
    Counts the number of parallelograms that can be formed with the given points.

    Parameters:
    n (int): The number of points.
    points (list of tuples): A list of tuples where each tuple represents the coordinates of a point.

    Returns:
    int: The number of parallelograms that can be formed.
    """
    count = Counter()
    
    for i in range(n):
        for j in range(i + 1, n):
            mid_x = points[i][0] + points[j][0]
            mid_y = points[i][1] + points[j][1]
            count[(mid_x, mid_y)] += 1
    
    ans = sum((i * (i - 1) // 2 for i in count.values()))
    return ans