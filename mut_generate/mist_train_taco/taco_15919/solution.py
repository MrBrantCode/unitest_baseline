"""
QUESTION:
Arpa is taking a geometry exam. Here is the last problem of the exam.

You are given three points a, b, c.

Find a point and an angle such that if we rotate the page around the point by the angle, the new position of a is the same as the old position of b, and the new position of b is the same as the old position of c.

Arpa is doubting if the problem has a solution or not (i.e. if there exists a point and an angle satisfying the condition). Help Arpa determine if the question has a solution or not.


-----Input-----

The only line contains six integers a_{x}, a_{y}, b_{x}, b_{y}, c_{x}, c_{y} (|a_{x}|, |a_{y}|, |b_{x}|, |b_{y}|, |c_{x}|, |c_{y}| ≤ 10^9). It's guaranteed that the points are distinct.


-----Output-----

Print "Yes" if the problem has a solution, "No" otherwise.

You can print each letter in any case (upper or lower).


-----Examples-----
Input
0 1 1 1 1 0

Output
Yes

Input
1 1 0 0 1000 1000

Output
No



-----Note-----

In the first sample test, rotate the page around (0.5, 0.5) by $90^{\circ}$.

In the second sample test, you can't find any solution.
"""

def has_rotation_solution(ax: int, ay: int, bx: int, by: int, cx: int, cy: int) -> str:
    """
    Determines if there exists a point and an angle such that rotating the page around the point by the angle
    results in the new position of point a being the old position of point b, and the new position of point b
    being the old position of point c.

    Parameters:
    ax (int): x-coordinate of point a
    ay (int): y-coordinate of point a
    bx (int): x-coordinate of point b
    by (int): y-coordinate of point b
    cx (int): x-coordinate of point c
    cy (int): y-coordinate of point c

    Returns:
    str: "Yes" if a solution exists, "No" otherwise.
    """
    ab = (ax - bx) * (ax - bx) + (ay - by) * (ay - by)
    bc = (cx - bx) * (cx - bx) + (cy - by) * (cy - by)
    line = (ax - cx) * (by - ay) == (bx - ax) * (ay - cy)
    
    if ab == bc and not line:
        return 'Yes'
    else:
        return 'No'