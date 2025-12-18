"""
QUESTION:
We have a set S of N points in a two-dimensional plane. The coordinates of the i-th point are (x_i, y_i). The N points have distinct x-coordinates and distinct y-coordinates.
For a non-empty subset T of S, let f(T) be the number of points contained in the smallest rectangle, whose sides are parallel to the coordinate axes, that contains all the points in T. More formally, we define f(T) as follows:
 - f(T) :=  (the number of integers i (1 \leq i \leq N) such that a \leq x_i \leq b and c \leq y_i \leq d, where a, b, c, and d are the minimum x-coordinate, the maximum x-coordinate, the minimum y-coordinate, and the maximum y-coordinate of the points in T)
Find the sum of f(T) over all non-empty subset T of S. Since it can be enormous, print the sum modulo 998244353.

-----Constraints-----
 - 1 \leq N \leq 2 \times 10^5
 - -10^9 \leq x_i, y_i \leq 10^9
 - x_i \neq x_j (i \neq j)
 - y_i \neq y_j (i \neq j)
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
x_1 y_1
:
x_N y_N

-----Output-----
Print the sum of f(T) over all non-empty subset T of S, modulo 998244353.

-----Sample Input-----
3
-1 3
2 1
3 -2

-----Sample Output-----
13

Let the first, second, and third points be P_1, P_2, and P_3, respectively. S = \{P_1, P_2, P_3\} has seven non-empty subsets, and f has the following values for each of them:
 - f(\{P_1\}) = 1
 - f(\{P_2\}) = 1
 - f(\{P_3\}) = 1
 - f(\{P_1, P_2\}) = 2
 - f(\{P_2, P_3\}) = 2
 - f(\{P_3, P_1\}) = 3
 - f(\{P_1, P_2, P_3\}) = 3
The sum of these is 13.
"""

def calculate_sum_of_f_over_subsets(points, mod=998244353):
    N = len(points)
    compression_dict_x = {a: ind for (ind, a) in enumerate(sorted(set([p[0] for p in points])))}
    points = [[compression_dict_x[x] + 1, y] for (x, y) in points]
    P_Y = sorted(points, key=lambda x: x[1])
    LEN = len(compression_dict_x)
    BIT = [0] * (LEN + 1)

    def update(v, w):
        while v <= LEN:
            BIT[v] += w
            v += v & -v

    def getvalue(v):
        ANS = 0
        while v != 0:
            ANS += BIT[v]
            v -= v & -v
        return ANS

    ANS = 4 * N + (pow(2, N, mod) - 1) * (N - 4) % mod
    for i in range(N):
        (x, y) = P_Y[i]
        left = getvalue(x)
        ANS = (ANS + pow(2, left, mod) + pow(2, i - left, mod) - 2) % mod
        update(x, 1)

    P_Y.reverse()
    BIT = [0] * (LEN + 1)
    for i in range(N):
        (x, y) = P_Y[i]
        left = getvalue(x)
        ANS = (ANS + pow(2, left, mod) + pow(2, i - left, mod) - 2) % mod
        update(x, 1)

    return ANS