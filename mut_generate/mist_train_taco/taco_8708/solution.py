"""
QUESTION:
Problem Statement

Circles Island is known for its mysterious shape: it is a completely flat island with its shape being a union of circles whose centers are on the $x$-axis and their inside regions.

The King of Circles Island plans to build a large square on Circles Island in order to celebrate the fiftieth anniversary of his accession. The King wants to make the square as large as possible. The whole area of the square must be on the surface of Circles Island, but any area of Circles Island can be used for the square. He also requires that the shape of the square is square (of course!) and at least one side of the square is parallel to the $x$-axis.

You, a minister of Circles Island, are now ordered to build the square. First, the King wants to know how large the square can be. You are given the positions and radii of the circles that constitute Circles Island. Answer the side length of the largest possible square.

$N$ circles are given in an ascending order of their centers' $x$-coordinates. You can assume that for all $i$ ($1 \le i \le N-1$), the $i$-th and $(i+1)$-st circles overlap each other. You can also assume that no circles are completely overlapped by other circles.

<image>

[fig.1 : Shape of Circles Island and one of the largest possible squares for test case #1 of sample input]

Input

The input consists of multiple datasets. The number of datasets does not exceed $30$. Each dataset is formatted as follows.

> $N$
> $X_1$ $R_1$
> :
> :
> $X_N$ $R_N$

The first line of a dataset contains a single integer $N$ ($1 \le N \le 50{,}000$), the number of circles that constitute Circles Island. Each of the following $N$ lines describes a circle. The $(i+1)$-st line contains two integers $X_i$ ($-100{,}000 \le X_i \le 100{,}000$) and $R_i$ ($1 \le R_i \le 100{,}000$). $X_i$ denotes the $x$-coordinate of the center of the $i$-th circle and $R_i$ denotes the radius of the $i$-th circle. The $y$-coordinate of every circle is $0$, that is, the center of the $i$-th circle is at ($X_i$, $0$).

You can assume the followings.

* For all $i$ ($1 \le i \le N-1$), $X_i$ is strictly less than $X_{i+1}$.
* For all $i$ ($1 \le i \le N-1$), the $i$-th circle and the $(i+1)$-st circle have at least one common point ($X_{i+1} - X_i \le R_i + R_{i+1}$).
* Every circle has at least one point that is not inside or on the boundary of any other circles.



The end of the input is indicated by a line containing a zero.

Output

For each dataset, output a line containing the side length of the square with the largest area. The output must have an absolute or relative error at most $10^{-4}$.

Sample Input


2
0 8
10 8
2
0 7
10 7
0

Output for the Sample Input


12.489995996796796
9.899494936611665





Example

Input

2
0 8
10 8
2
0 7
10 7
0


Output

12.489995996796796
9.899494936611665
"""

def find_largest_square_side_length(circles):
    if not circles:
        return 0.0

    N = len(circles)
    e = 2 ** 0.5 / 2
    r_min = max((r * e for (x, r) in circles))
    r_max = max((r for (x, r) in circles))
    H = []

    for i in range(N - 1):
        (x0, r0) = circles[i]
        (x1, r1) = circles[i + 1]
        dx = x1 - x0
        l = (r0 ** 2 + dx ** 2 - r1 ** 2) / (2 * dx)
        h = (r0 ** 2 - l ** 2) ** 0.5
        H.append(h)

    def check(h):
        k = -1
        for i in range(N):
            (xi, ri) = circles[i]
            if k == -1:
                if h <= ri:
                    k = i
            elif H[i - 1] < h:
                if k != -1:
                    (xp, rp) = circles[k]
                    (xq, rq) = circles[i - 1]
                    x0 = xp - (rp ** 2 - h ** 2) ** 0.5
                    x1 = xq + (rq ** 2 - h ** 2) ** 0.5
                    if x1 - x0 >= 2 * h:
                        return True
                if h <= ri:
                    k = i
                else:
                    k = -1
        if k == -1:
            return False
        (xp, rp) = circles[k]
        (xq, rq) = circles[N - 1]
        x0 = xp - (rp ** 2 - h ** 2) ** 0.5
        x1 = xq + (rq ** 2 - h ** 2) ** 0.5
        return x1 - x0 >= 2 * h

    left = r_min
    right = r_max + 1
    EPS = 1e-05

    while right - left > EPS:
        mid = (left + right) / 2
        if check(mid):
            left = mid
        else:
            right = mid

    return left * 2