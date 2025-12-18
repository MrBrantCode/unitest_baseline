"""
QUESTION:
Bob wants to put a new bargaining table in his office. To do so he measured the office room thoroughly and drew its plan: Bob's office room is a rectangular room n × m meters. Each square meter of the room is either occupied by some furniture, or free. A bargaining table is rectangular, and should be placed so, that its sides are parallel to the office walls. Bob doesn't want to change or rearrange anything, that's why all the squares that will be occupied by the table should be initially free. Bob wants the new table to sit as many people as possible, thus its perimeter should be maximal. Help Bob find out the maximum possible perimeter of a bargaining table for his office.

Input

The first line contains 2 space-separated numbers n and m (1 ≤ n, m ≤ 25) — the office room dimensions. Then there follow n lines with m characters 0 or 1 each. 0 stands for a free square meter of the office room. 1 stands for an occupied square meter. It's guaranteed that at least one square meter in the room is free.

Output

Output one number — the maximum possible perimeter of a bargaining table for Bob's office room.

Examples

Input

3 3
000
010
000


Output

8


Input

5 4
1100
0000
0000
0000
0000


Output

16
"""

def max_bargaining_table_perimeter(n, m, office_layout):
    ans = 0
    for x1 in range(m):
        for x2 in range(x1, m):
            for y1 in range(n):
                for y2 in range(y1, n):
                    z = 0
                    for k in range(y1, y2 + 1):
                        z += sum(office_layout[k][x1:x2 + 1])
                    if z == 0:
                        ans = max(ans, 2 * (x2 - x1 + 1 + y2 - y1 + 1))
    return ans