"""
QUESTION:
Mr. Bender has a digital table of size n × n, each cell can be switched on or off. He wants the field to have at least c switched on squares. When this condition is fulfilled, Mr Bender will be happy.

We'll consider the table rows numbered from top to bottom from 1 to n, and the columns — numbered from left to right from 1 to n. Initially there is exactly one switched on cell with coordinates (x, y) (x is the row number, y is the column number), and all other cells are switched off. Then each second we switch on the cells that are off but have the side-adjacent cells that are on.

For a cell with coordinates (x, y) the side-adjacent cells are cells with coordinates (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1).

In how many seconds will Mr. Bender get happy?


-----Input-----

The first line contains four space-separated integers n, x, y, c (1 ≤ n, c ≤ 10^9; 1 ≤ x, y ≤ n; c ≤ n^2).


-----Output-----

In a single line print a single integer — the answer to the problem.


-----Examples-----
Input
6 4 3 1

Output
0

Input
9 3 8 10

Output
2



-----Note-----

Initially the first test has one painted cell, so the answer is 0. In the second test all events will go as is shown on the figure. [Image].
"""

def calculate_happiness_seconds(n, x, y, c):
    def out_new(s, sx):
        if sx < s:
            return (s - sx) * 2 - 1
        else:
            return 0

    def in_new(s, sx):
        if sx < s:
            return s - sx
        else:
            return 0

    x1 = min(x - 1, n - x)
    x2 = n - x1 - 1
    y1 = min(y - 1, n - y)
    y2 = n - y1 - 1
    i1 = x1 + y1 + 1
    i2 = min(y1 + x2, y2 + x1) + 1
    i3 = max(y1 + x2, y2 + x1) + 1
    o1 = min(x1, y1)
    o2 = min(max(x1, y1), min(y2, x2))
    o3 = max(max(x1, y1), min(y2, x2))
    o4 = max(y2, x2)
    
    inside = 0
    out = 0
    s = 0
    current = 1
    Happy = False
    
    if c == 1:
        return 0
    
    while not Happy:
        s += 1
        new = (s + 1) * 4 - 4
        out = out + out_new(s, o1) + out_new(s, o2) + out_new(s, o3) + out_new(s, o4)
        inside = inside + in_new(s, i1) + in_new(s, i2) + in_new(s, i3)
        current = current + new
        test = current - out + inside
        if test >= c:
            Happy = True
    
    return s