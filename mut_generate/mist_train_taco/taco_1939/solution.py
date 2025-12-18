"""
QUESTION:
Chef loves squares! You are given N points with integers coordinates, Chef asks you to find out how many points he should add to these set of N points, so that one could create at least one square having its vertices from the points of the resulting set. Note that the square created need not to be parallel to the axis.

-----Input-----
The first line contains singe integer N. 
Each of next N lines contains two integers Xi and Yi denotine the coordinates of i-th point. 

-----Output-----
In a single line print single integer - the minimal number of points Chef need to paint to receive at least one square. 

-----Constraints-----
- 0 ≤ N ≤ 2000
- -10^6 ≤ Xi, Yi ≤ 10^6
- There are NO coincided points

-----Example-----
Input:
3
0 0
2 2
3 3

Output:
2

Input:
5
0 0
100 100
200 200
100 0
0 100

Output:
0

-----Explanation-----
For the first example Chef can add points (2, 0), (0, 2) or (2, 3), (3, 2)
For the second example Chef already has square (0, 0), (100, 0), (0, 100), (100, 100).
"""

def min_points_to_form_square(points):
    set_points = set(points)
    n = len(points)
    answered = False
    result = 0

    if n == 0:
        return 4

    if n >= 4:
        for i in range(n):
            for j in range(i + 1, n):
                (p_a, p_b) = (points[i], points[j])
                (dx, dy) = (p_a[0] - p_b[0], p_a[1] - p_b[1])
                if (p_b[0] - dy, p_b[1] + dx) in set_points and (p_b[0] + dx - dy, p_b[1] + dx + dy) in set_points or \
                   (p_b[0] + dy, p_b[1] - dx) in set_points and (p_b[0] + dx + dy, p_b[1] - dx + dy) in set_points:
                    return 0
                    answered = True

    if not answered and n >= 3:
        for i in range(n):
            for j in range(i + 1, n):
                (p_a, p_b) = (points[i], points[j])
                (dx, dy) = (p_a[0] - p_b[0], p_a[1] - p_b[1])
                if (p_b[0] - dy, p_b[1] + dx) in set_points or (p_b[0] + dx - dy, p_b[1] + dx + dy) in set_points or \
                   (p_b[0] + dy, p_b[1] - dx) in set_points or (p_b[0] + dx + dy, p_b[1] - dx + dy) in set_points:
                    return 1
                    answered = True

    if not answered and n >= 2:
        return 2

    if not answered:
        return 3

    return result