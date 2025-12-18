"""
QUESTION:
Vanya decided to walk in the field of size n × n cells. The field contains m apple trees, the i-th apple tree is at the cell with coordinates (xi, yi). Vanya moves towards vector (dx, dy). That means that if Vanya is now at the cell (x, y), then in a second he will be at cell <image>. The following condition is satisfied for the vector: <image>, where <image> is the largest integer that divides both a and b. Vanya ends his path when he reaches the square he has already visited. 

Vanya wonders, from what square of the field he should start his path to see as many apple trees as possible.

Input

The first line contains integers n, m, dx, dy(1 ≤ n ≤ 106, 1 ≤ m ≤ 105, 1 ≤ dx, dy ≤ n) — the size of the field, the number of apple trees and the vector of Vanya's movement. Next m lines contain integers xi, yi (0 ≤ xi, yi ≤ n - 1) — the coordinates of apples. One cell may contain multiple apple trees.

Output

Print two space-separated numbers — the coordinates of the cell from which you should start your path. If there are several answers you are allowed to print any of them.

Examples

Input

5 5 2 3
0 0
1 2
1 3
2 4
3 1


Output

1 3


Input

2 3 1 1
0 0
0 1
1 1


Output

0 0

Note

In the first sample Vanya's path will look like: (1, 3) - (3, 1) - (0, 4) - (2, 2) - (4, 0) - (1, 3)

In the second sample: (0, 0) - (1, 1) - (0, 0)
"""

def find_optimal_starting_point(n, m, dx, dy, apple_trees):
    x = y = 0
    a = [0] * n
    c = [0] * n
    
    # Calculate the y-coordinates for each x-coordinate after one full cycle
    for i in range(1, n):
        x = (x + dx) % n
        y = (y + dy) % n
        a[x] = y
    
    # Count the number of apple trees for each starting point
    for (xi, yi) in apple_trees:
        index = (yi - a[xi] + n) % n
        c[index] += 1
    
    # Find the starting point with the maximum number of apple trees
    ans = 0
    for i in range(n):
        if c[i] > c[ans]:
            ans = i
    
    # The optimal starting point is (0, ans)
    return (0, ans)