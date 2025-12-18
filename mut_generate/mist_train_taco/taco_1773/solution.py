"""
QUESTION:
You are given a set of N distinct points P_{1}, P_{2}, P_{3}, \ldots, P_{N} on a 2-D plane.

A triplet (i, j, k) is called a holy triplet if
1 ≤ i < j < k ≤ N
P_{i}, P_{j} and P_{k} are non-collinear and
Any two of the points P_{i}, P_{j} and P_{k} are [antipodal] points of the circle that passes through all three of them.

Two points on a circle are said to be antipodal points of the circle if they are diametrically opposite to each other.

Find the total number of holy triplets.

------ Input Format ------ 

- The first line contains a single integer T - the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer N - the number of points.
- Each of the next N lines contains two space separated integers x_{i} and y_{i}, denoting the co-ordinates of i-th point P_{i}.

------ Output Format ------ 

For each test case output a single line denoting the number of holy triplets.

------ Constraints ------ 

$1 ≤ T ≤ 10$
$3 ≤ N ≤ 2000$
- Sum of $N$ over all test cases does not exceed $2000$
$-10^{9} ≤ x_{i}, y_{i} ≤ 10^{9}$
- All points $P_{1}, P_{2}, \ldots, P_{N}$ in each test case are distinct.

----- Sample Input 1 ------ 
1
4
0 1
0 -1
1 0
-1 0
----- Sample Output 1 ------ 
4
----- explanation 1 ------ 
Test case 1: The holy triplets in this case are
$$
\begin{array}{|c|c|c|c|}
\hline
\textbf{Holy Triplet} & 1 ≤ i < j < k ≤ N & \textbf{Non collinear} & \textbf{Antipodal points} \\ 
\hline
(1, 2, 3) & \checkmark & \checkmark & 1 \text{ and } 2 \\
\hline
(1, 2, 4) & \checkmark & \checkmark & 1 \text{ and } 2 \\
\hline
(1, 3, 4) & \checkmark & \checkmark & 3 \text{ and } 4  \\
\hline
(2, 3, 4) & \checkmark & \checkmark & 3 \text{ and } 4 \\
\hline
\end{array}
$$
"""

def count_holy_triplets(points):
    def slope(x1, y1, x2, y2):
        if x2 - x1 == 0:
            return 'inf'
        return float(y2 - y1) / (x2 - x1)

    n = len(points)
    c = 0

    for j in range(n):
        m = {}
        for k in range(n):
            if k == j:
                continue
            s = slope(points[j][0], points[j][1], points[k][0], points[k][1])
            if s in m:
                m[s] += 1
            else:
                m[s] = 1

        for k in m:
            if k == 'inf':
                if 0 in m:
                    c += m[0] * m[k]
                continue
            if k == 0:
                if 'inf' in m:
                    c += m['inf'] * m[k]
                continue
            if -1 / k in m:
                c += m[-1 / k] * m[k]

    return c // 2