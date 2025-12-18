"""
QUESTION:
There are n points on the plane, the i-th of which is at (x_i, y_i). Tokitsukaze wants to draw a strange rectangular area and pick all the points in the area.

The strange area is enclosed by three lines, x = l, y = a and x = r, as its left side, its bottom side and its right side respectively, where l, r and a can be any real numbers satisfying that l < r. The upper side of the area is boundless, which you can regard as a line parallel to the x-axis at infinity. The following figure shows a strange rectangular area.

<image>

A point (x_i, y_i) is in the strange rectangular area if and only if l < x_i < r and y_i > a. For example, in the above figure, p_1 is in the area while p_2 is not.

Tokitsukaze wants to know how many different non-empty sets she can obtain by picking all the points in a strange rectangular area, where we think two sets are different if there exists at least one point in one set of them but not in the other.

Input

The first line contains a single integer n (1 ≤ n ≤ 2 × 10^5) — the number of points on the plane.

The i-th of the next n lines contains two integers x_i, y_i (1 ≤ x_i, y_i ≤ 10^9) — the coordinates of the i-th point.

All points are distinct.

Output

Print a single integer — the number of different non-empty sets of points she can obtain.

Examples

Input

3
1 1
1 2
1 3


Output

3


Input

3
1 1
2 1
3 1


Output

6


Input

4
2 1
2 2
3 1
3 2


Output

6

Note

For the first example, there is exactly one set having k points for k = 1, 2, 3, so the total number is 3.

For the second example, the numbers of sets having k points for k = 1, 2, 3 are 3, 2, 1 respectively, and their sum is 6.

For the third example, as the following figure shows, there are

  * 2 sets having one point; 
  * 3 sets having two points; 
  * 1 set having four points. 



Therefore, the number of different non-empty sets in this example is 2 + 3 + 0 + 1 = 6.

<image>
"""

def count_strange_rectangular_sets(points):
    n = len(points)
    points.sort()
    cts = [0] * (n + 1)
    x_map = {}
    ctr = 0
    for p in points:
        if p[0] not in x_map:
            ctr += 1
            x_map[p[0]] = ctr
        cts[ctr] += 1
    points = [(x_map[p[0]], p[1]) for p in points]
    collected = defaultdict(list)
    for p in points:
        collected[p[1]].append(p)
    bit = [0] * (n + 1)

    def query(i):
        ans = 0
        while i > 0:
            ans += bit[i]
            i -= i & -i
        return ans

    def update(i, x):
        while i <= n:
            bit[i] += x
            i += i & -i

    for i in range(1, ctr + 1):
        update(i, 1)
    ans = 0
    for (y, y_pts) in sorted(collected.items()):
        total = query(n)
        ans += total * (total + 1) // 2
        prev_x = 0
        for p in y_pts:
            local = query(p[0]) - (query(prev_x) if prev_x else 0) - 1
            ans -= local * (local + 1) // 2
            prev_x = p[0]
        local = total - query(prev_x)
        ans -= local * (local + 1) // 2
        for p in y_pts:
            cts[p[0]] -= 1
            if cts[p[0]] == 0:
                update(p[0], -1)
    return ans