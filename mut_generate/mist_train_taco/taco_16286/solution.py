"""
QUESTION:
You are given a rectangle grid. That grid's size is n × m. Let's denote the coordinate system on the grid. So, each point on the grid will have coordinates — a pair of integers (x, y) (0 ≤ x ≤ n, 0 ≤ y ≤ m).

Your task is to find a maximum sub-rectangle on the grid (x1, y1, x2, y2) so that it contains the given point (x, y), and its length-width ratio is exactly (a, b). In other words the following conditions must hold: 0 ≤ x1 ≤ x ≤ x2 ≤ n, 0 ≤ y1 ≤ y ≤ y2 ≤ m, <image>.

The sides of this sub-rectangle should be parallel to the axes. And values x1, y1, x2, y2 should be integers.

<image>

If there are multiple solutions, find the rectangle which is closest to (x, y). Here "closest" means the Euclid distance between (x, y) and the center of the rectangle is as small as possible. If there are still multiple solutions, find the lexicographically minimum one. Here "lexicographically minimum" means that we should consider the sub-rectangle as sequence of integers (x1, y1, x2, y2), so we can choose the lexicographically minimum one.

Input

The first line contains six integers n, m, x, y, a, b (1 ≤ n, m ≤ 109, 0 ≤ x ≤ n, 0 ≤ y ≤ m, 1 ≤ a ≤ n, 1 ≤ b ≤ m).

Output

Print four integers x1, y1, x2, y2, which represent the founded sub-rectangle whose left-bottom point is (x1, y1) and right-up point is (x2, y2).

Examples

Input

9 9 5 5 2 1


Output

1 3 9 7


Input

100 100 52 50 46 56


Output

17 8 86 92
"""

def gcd(a, b):
    while a:
        (a, b) = (b % a, a)
    return b

def find_max_sub_rectangle(n, m, x, y, a, b):
    g = gcd(a, b)
    a //= g
    b //= g
    k = min(n // a, m // b)
    w = k * a
    h = k * b
    ans = [x - w + w // 2, y - h + h // 2, x + w // 2, y + h // 2]
    
    if ans[0] < 0:
        ans[2] -= ans[0]
        ans[0] = 0
    if ans[1] < 0:
        ans[3] -= ans[1]
        ans[1] = 0
    if ans[2] > n:
        ans[0] -= ans[2] - n
        ans[2] = n
    if ans[3] > m:
        ans[1] -= ans[3] - m
        ans[3] = m
    
    return tuple(ans)