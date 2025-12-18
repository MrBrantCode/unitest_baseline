"""
QUESTION:
Polycarp is very fond of playing the game Minesweeper. Recently he found a similar game and there are such rules.

There are mines on the field, for each the coordinates of its location are known ($x_i, y_i$). Each mine has a lifetime in seconds, after which it will explode. After the explosion, the mine also detonates all mines vertically and horizontally at a distance of $k$ (two perpendicular lines). As a result, we get an explosion on the field in the form of a "plus" symbol ('+'). Thus, one explosion can cause new explosions, and so on.

Also, Polycarp can detonate anyone mine every second, starting from zero seconds. After that, a chain reaction of explosions also takes place. Mines explode instantly and also instantly detonate other mines according to the rules described above.

Polycarp wants to set a new record and asks you to help him calculate in what minimum number of seconds all mines can be detonated.


-----Input-----

The first line of the input contains an integer $t$ ($1 \le t \le 10^4$) — the number of test cases in the test.

An empty line is written in front of each test suite.

Next comes a line that contains integers $n$ and $k$ ($1 \le n \le 2 \cdot 10^5$, $0 \le k \le 10^9$) — the number of mines and the distance that hit by mines during the explosion, respectively.

Then $n$ lines follow, the $i$-th of which describes the $x$ and $y$ coordinates of the $i$-th mine and the time until its explosion ($-10^9 \le x, y \le 10^9$, $0 \le timer \le 10^9$). It is guaranteed that all mines have different coordinates.

It is guaranteed that the sum of the values $n$ over all test cases in the test does not exceed $2 \cdot 10^5$.


-----Output-----

Print $t$ lines, each of the lines must contain the answer to the corresponding set of input data  — the minimum number of seconds it takes to explode all the mines.


-----Examples-----

Input
3

5 0
0 0 1
0 1 4
1 0 2
1 1 3
2 2 9

5 2
0 0 1
0 1 4
1 0 2
1 1 3
2 2 9

6 1
1 -1 3
0 -1 9
0 1 7
-1 0 1
-1 1 9
-1 -1 7
Output
2
1
0


-----Note-----

Picture from examples

First example:

$0$ second: we explode a mine at the cell $(2, 2)$, it does not detonate any other mine since $k=0$.

$1$ second: we explode the mine at the cell $(0, 1)$, and the mine at the cell $(0, 0)$ explodes itself.

$2$ second: we explode the mine at the cell $(1, 1)$, and the mine at the cell $(1, 0)$ explodes itself.

Second example:

$0$ second: we explode a mine at the cell $(2, 2)$ we get:

$1$ second: the mine at coordinate $(0, 0)$ explodes and since $k=2$ the explosion detonates mines at the cells $(0, 1)$ and $(1, 0)$, and their explosions detonate the mine at the cell $(1, 1)$ and there are no mines left on the field.
"""

def calculate_minimum_detonation_time(t, test_cases):
    class SDS:
        def __init__(self, n, mins):
            self.n = n
            self.parents = [i for i in range(n)]
            self.mins = mins

        def find(self, i):
            if self.parents[i] != i:
                self.parents[i] = self.find(self.parents[i])
            return self.parents[i]

        def union(self, i, j):
            (i, j) = (self.find(i), self.find(j))
            if i == j:
                return
            self.parents[j] = i
            self.mins[i] = min(self.mins[j], self.mins[i])

        def tolist(self):
            result = []
            for i in range(self.n):
                if i == self.parents[i]:
                    result.append(self.mins[i])
            return (sorted(result), len(result))

    result = []
    for test_case in test_cases:
        n, k, mines = test_case
        sds = SDS(n, list(map(lambda x: x[2], mines)))
        mines = [list(mine) + [i] for i, mine in enumerate(mines)]
        mines.sort(key=lambda x: (x[0], x[1]))
        (i, x, y) = (None, None, None)
        for mine in mines:
            if x == mine[0] and abs(mine[1] - y) <= k:
                sds.union(mine[3], i)
            (i, x, y) = (mine[3], mine[0], mine[1])
        mines.sort(key=lambda x: (x[1], x[0]))
        (i, x, y) = (None, None, None)
        for mine in mines:
            if y == mine[1] and abs(mine[0] - x) <= k:
                sds.union(mine[3], i)
            (i, x, y) = (mine[3], mine[0], mine[1])
        (mins, length) = sds.tolist()
        answer = length - 1
        for i in range(length):
            answer = min(answer, max(mins[i], length - i - 2))
        result.append(answer)
    return result