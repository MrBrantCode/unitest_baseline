"""
QUESTION:
You are given n points on a plane. All points are different.

Find the number of different groups of three points (A, B, C) such that point B is the middle of segment AC. 

The groups of three points are considered unordered, that is, if point B is the middle of segment AC, then groups (A, B, C) and (C, B, A) are considered the same.

Input

The first line contains a single integer n (3 ≤ n ≤ 3000) — the number of points. 

Next n lines contain the points. The i-th line contains coordinates of the i-th point: two space-separated integers xi, yi ( - 1000 ≤ xi, yi ≤ 1000).

It is guaranteed that all given points are different.

Output

Print the single number — the answer to the problem. 

Examples

Input

3
1 1
2 2
3 3


Output

1


Input

3
0 0
-1 0
0 1


Output

0
"""

def count_middle_points(n, points):
    # Initialize a 2D list to keep track of the presence of points
    cords = [[False] * 2001 for _ in range(2001)]
    
    # Mark the points in the cords array
    for (x, y) in points:
        cords[x + 1000][y + 1000] = True
    
    count = 0
    
    # Iterate over all pairs of points to find middle points
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x3, y3 = points[j]
            x2 = (x1 + x3) // 2
            y2 = (y1 + y3) // 2
            
            # Check if the middle point exists
            if (x1 + x3) % 2 == 0 and (y1 + y3) % 2 == 0 and cords[x2 + 1000][y2 + 1000]:
                count += 1
    
    return count