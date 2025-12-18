"""
QUESTION:
Chef wants to gift his girlfriend a necklace made of beads. The beads can be made of either Stone, Glass, Quartz, Ruby or Diamond (he need not use all five types of beads) .

Each bead has a value associated with its beauty as follows

-2 for Stone
-1 for Glass
0 for Quartz 
1 for Ruby
2 for Diamond

Each bead also has a cost given by  S, G, Q, R and D for the respective bead.

There are q queries for you. In each query chef wants to know the minimum cost for creating a necklace using exactly X beads and overall beauty of Y.

Overall beauty Y is defined as the sum of beauty of each bead used in the necklace.

Since you’re a great programmer, he wants you to answer each query as soon as possible.

------ Input ------

First line contains 5 space separated integers S, G, Q, R, D, the respective cost of beads.
Next line contains q the number of queries
next q lines had two integers X and Y , the number of beads to be used and the overall beauty

------ Output ------

for each query output the answer in a new line
output the minimum cost if it exists otherwise print -1

------ Constrains ------

$1 ≤ q ≤ 5*10^{5}$
$0 ≤ S, G, Q, R, D ≤ 10^{6}$
$0 ≤ X ≤ 100$
$-200 ≤ Y ≤ 200$

------ Subtasks ------
10 points : $0 ≤ X ≤ 2$
20 points : $ q=1 $
70 points : original constrains	

------ Sample Input ------

1 2 2 3 4

3

2 0

1 -2

3 6

------ Sample Output ------

4

1

12

------ Explanation ------

in the first query we can take (stone,diamond), (glass,ruby), (quarts,quarts)
but the minimum cost would be if we took quarts and quarts which is 4

second query there is only one way that is to take one stone and the cost is 1

third query also there is only one way to take three diamonds and the cost is 12
"""

def calculate_minimum_cost(costs, beads_count, total_beauty):
    beauty = [-2, -1, 0, 1, 2]
    inf = float('inf')
    dp = [[-1] * 801 for _ in range(101)]

    def f(x, y):
        if abs(y) > 2 * x:
            dp[x][y + 400] = inf
            return inf
        if dp[x][y + 400] != -1:
            return dp[x][y + 400]
        if x == 0:
            dp[x][y + 400] = 0 if y == 0 else inf
            return dp[x][y + 400]
        dp[x][y + 400] = costs[0] + f(x - 1, y + 2)
        for i in range(1, 5):
            dp[x][y + 400] = min(dp[x][y + 400], f(x - 1, y - beauty[i]) + costs[i])
        return dp[x][y + 400]

    for i in range(101):
        for j in range(-400, 401):
            f(i, j)

    ans = f(beads_count, total_beauty)
    return -1 if ans == inf else ans