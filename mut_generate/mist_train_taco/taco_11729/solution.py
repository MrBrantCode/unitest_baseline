"""
QUESTION:
There are three points marked on the coordinate plane. The goal is to make a simple polyline, without self-intersections and self-touches, such that it passes through all these points. Also, the polyline must consist of only segments parallel to the coordinate axes. You are to find the minimum number of segments this polyline may consist of.


-----Input-----

Each of the three lines of the input contains two integers. The i-th line contains integers x_{i} and y_{i} ( - 10^9 ≤ x_{i}, y_{i} ≤ 10^9) — the coordinates of the i-th point. It is guaranteed that all points are distinct.


-----Output-----

Print a single number — the minimum possible number of segments of the polyline.


-----Examples-----
Input
1 -1
1 1
1 2

Output
1

Input
-1 -1
-1 3
4 3

Output
2

Input
1 1
2 3
3 2

Output
3



-----Note-----

The variant of the polyline in the first sample: [Image] The variant of the polyline in the second sample: $1$ The variant of the polyline in the third sample: $\because$
"""

def minimum_segments_for_polyline(ax, ay, bx, by, cx, cy):
    if ax == bx == cx or ay == by == cy:
        return 1
    elif ax == bx and (cy <= min(ay, by) or cy >= max(ay, by)):
        return 2
    elif ax == cx and (by <= min(ay, cy) or by >= max(ay, cy)):
        return 2
    elif cx == bx and (ay <= min(cy, by) or ay >= max(cy, by)):
        return 2
    elif ay == by and (cx <= min(ax, bx) or cx >= max(ax, bx)):
        return 2
    elif ay == cy and (bx <= min(ax, cx) or bx >= max(ax, cx)):
        return 2
    elif cy == by and (ax <= min(cx, bx) or ax >= max(cx, bx)):
        return 2
    else:
        return 3