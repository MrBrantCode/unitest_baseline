"""
QUESTION:
You are given a n × m field consisting only of periods ('.') and asterisks ('*'). Your task is to count all right triangles with two sides parallel to the square sides, whose vertices are in the centers of '*'-cells. A right triangle is a triangle in which one angle is a right angle (that is, a 90 degree angle).

Input

The first line contains two positive integer numbers n and m (1 ≤ n, m ≤ 1000). The following n lines consist of m characters each, describing the field. Only '.' and '*' are allowed.

Output

Output a single number — total number of square triangles in the field. Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cout (also you may use %I64d).

Examples

Input

2 2
**
*.


Output

1


Input

3 4
*..*
.**.
*.**


Output

9
"""

def count_right_triangles(n, m, grid):
    a = [[0 for _ in range(m)] for _ in range(n)]
    b = [[0 for _ in range(m)] for _ in range(n)]
    
    # Fill the prefix sums arrays
    for i in range(n):
        for j in range(m):
            a[i][j] = a[i][j - 1] + (grid[i][j] == '*')
            if i > 0:
                b[i][j] = b[i - 1][j]
            b[i][j] += (grid[i][j] == '*')
    
    ans = 0
    
    # Count the right triangles
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                l = r = u = d = 0
                if j > 0:
                    l = a[i][j - 1]
                r = a[i][-1] - a[i][j]
                if i > 0:
                    u = b[i - 1][j]
                d = b[-1][j] - b[i][j]
                ans += (l + r) * (u + d)
    
    return ans