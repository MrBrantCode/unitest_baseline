"""
QUESTION:
You are given N points on a plane. Write a program which will find the sum of squares of distances between all pairs of points.

Input

The first line of input contains one integer number N (1 ≤ N ≤ 100 000) — the number of points. Each of the following N lines contain two integer numbers X and Y ( - 10 000 ≤ X, Y ≤ 10 000) — the coordinates of points. Two or more points may coincide.

Output

The only line of output should contain the required sum of squares of distances between all pairs of points.

Examples

Input

4
1 1
-1 -1
1 -1
-1 1


Output

32
"""

def calculate_sum_of_squares_of_distances(points):
    n = len(points)
    if n < 2:
        return 0
    
    n_1 = n - 1
    total_distance = 0
    Xs = []
    Ys = []
    xs = []
    ys = []
    x_addition = 0
    y_addition = 0
    
    for x, y in points:
        Xs.append(n_1 * x * x)
        Ys.append(n_1 * y * y)
        xs.append(x)
        ys.append(y)
        x_addition += x
        y_addition += y
    
    for index in range(n):
        x_addition -= xs[index]
        subtract = 2 * xs[index] * x_addition
        total_distance += Xs[index] - subtract
        
        y_addition -= ys[index]
        subtract = 2 * ys[index] * y_addition
        total_distance += Ys[index] - subtract
    
    return total_distance