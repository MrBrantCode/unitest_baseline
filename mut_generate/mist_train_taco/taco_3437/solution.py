"""
QUESTION:
There is a board with a grid consisting of n rows and m columns, the rows are numbered from 1 from top to bottom and the columns are numbered from 1 from left to right. In this grid we will denote the cell that lies on row number i and column number j as (i, j).

A group of six numbers (a, b, c, d, x0, y0), where 0 ≤ a, b, c, d, is a cross, and there is a set of cells that are assigned to it. Cell (x, y) belongs to this set if at least one of two conditions are fulfilled:

  * |x0 - x| ≤ a and |y0 - y| ≤ b
  * |x0 - x| ≤ c and |y0 - y| ≤ d

<image> The picture shows the cross (0, 1, 1, 0, 2, 3) on the grid 3 × 4. 

Your task is to find the number of different groups of six numbers, (a, b, c, d, x0, y0) that determine the crosses of an area equal to s, which are placed entirely on the grid. The cross is placed entirely on the grid, if any of its cells is in the range of the grid (that is for each cell (x, y) of the cross 1 ≤ x ≤ n; 1 ≤ y ≤ m holds). The area of the cross is the number of cells it has.

Note that two crosses are considered distinct if the ordered groups of six numbers that denote them are distinct, even if these crosses coincide as sets of points.

Input

The input consists of a single line containing three integers n, m and s (1 ≤ n, m ≤ 500, 1 ≤ s ≤ n·m). The integers are separated by a space.

Output

Print a single integer — the number of distinct groups of six integers that denote crosses with area s and that are fully placed on the n × m grid.

Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is preferred to use the cin, cout streams or the %I64d specifier.

Examples

Input

2 2 1


Output

4


Input

3 4 5


Output

4

Note

In the first sample the sought groups of six numbers are: (0, 0, 0, 0, 1, 1), (0, 0, 0, 0, 1, 2), (0, 0, 0, 0, 2, 1), (0, 0, 0, 0, 2, 2).

In the second sample the sought groups of six numbers are: (0, 1, 1, 0, 2, 2), (0, 1, 1, 0, 2, 3), (1, 0, 0, 1, 2, 2), (1, 0, 0, 1, 2, 3).
"""

def count_distinct_crosses(n, m, s):
    def ways(h, w, area):
        if area == h * w:
            return 2 * ((h + 1) // 2 * (w + 1) // 2) - 1
        if area > h * w:
            return 0
        if area < h + w - 1:
            return 0
        area = h * w - area
        if area % 4 != 0:
            return 0
        area //= 4
        ans = 0
        h //= 2
        w //= 2
        for a in range(1, h + 1):
            if area % a == 0 and area // a <= w:
                ans += 1
        return ans * 2

    ans = 0
    for h in range(1, n + 1, 2):
        for w in range(1, m + 1, 2):
            ans += ways(h, w, s) * (n - h + 1) * (m - w + 1)
    return ans