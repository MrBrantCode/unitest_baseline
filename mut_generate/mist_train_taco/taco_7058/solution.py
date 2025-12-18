"""
QUESTION:
Snuke is playing a puzzle game.
In this game, you are given a rectangular board of dimensions R × C, filled with numbers. Each integer i from 1 through N is written twice, at the coordinates (x_{i,1},y_{i,1}) and (x_{i,2},y_{i,2}).
The objective is to draw a curve connecting the pair of points where the same integer is written, for every integer from 1 through N.
Here, the curves may not go outside the board or cross each other.
Determine whether this is possible.

-----Constraints-----
 - 1 ≤ R,C ≤ 10^8
 - 1 ≤ N ≤ 10^5
 - 0 ≤ x_{i,1},x_{i,2} ≤ R(1 ≤ i ≤ N)
 - 0 ≤ y_{i,1},y_{i,2} ≤ C(1 ≤ i ≤ N)
 - All given points are distinct.
 - All input values are integers.

-----Input-----
Input is given from Standard Input in the following format:
R C N
x_{1,1} y_{1,1} x_{1,2} y_{1,2}
:
x_{N,1} y_{N,1} x_{N,2} y_{N,2}

-----Output-----
Print YES if the objective is achievable; print NO otherwise.

-----Sample Input-----
4 2 3
0 1 3 1
1 1 4 1
2 0 2 2

-----Sample Output-----
YES


The above figure shows a possible solution.
"""

def is_puzzle_solvable(R, C, N, points):
    def edge(x, y):
        return x == 0 or x == R or y == 0 or (y == C)

    def flat(x, y):
        assert edge(x, y)
        if y == 0:
            return x
        elif x == R:
            return R + y
        elif y == C:
            return R + C + (R - x)
        else:
            assert x == 0
            return 2 * R + C + (C - y)

    ps = []
    for i in range(N):
        (x1, y1, x2, y2) = points[i]
        if edge(x1, y1) and edge(x2, y2):
            ps.append((flat(x1, y1), i))
            ps.append((flat(x2, y2), i))

    ps.sort()
    stack = []
    for (_, i) in ps:
        if len(stack) > 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    return len(stack) == 0