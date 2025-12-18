"""
QUESTION:
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.
If there isn't any rectangle, return 0.
 

Example 1:
Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4


Example 2:
Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

 
Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
"""

def min_area_rectangle(points):
    d = defaultdict(set)
    (rset, cset, N, ans) = (set(), set(), len(points), float('inf'))
    for (r, c) in points:
        rset.add(r)
        cset.add(c)
    (Nr, Nc) = (len(rset), len(cset))
    if Nr == 1 or Nc == 1:
        return 0
    elif Nr < Nc:
        for (r, c) in points:
            d[r].add(c)
    else:
        for (r, c) in points:
            d[c].add(r)
    A = sorted(d.keys())
    for (i, r1) in enumerate(A):
        cols1 = d[r1]
        for r2 in A[i + 1:]:
            cols2 = d[r2]
            s = sorted(cols1 & cols2)
            for (c1, c2) in zip(s[:-1], s[1:]):
                area = abs((r1 - r2) * (c1 - c2))
                if area < ans:
                    ans = area
    return ans if ans < float('inf') else 0