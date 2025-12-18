"""
QUESTION:
It is the middle of 2018 and Maria Stepanovna, who lives outside Krasnokamensk (a town in Zabaikalsky region), wants to rent three displays to highlight an important problem.

There are $n$ displays placed along a road, and the $i$-th of them can display a text with font size $s_i$ only. Maria Stepanovna wants to rent such three displays with indices $i < j < k$ that the font size increases if you move along the road in a particular direction. Namely, the condition $s_i < s_j < s_k$ should be held.

The rent cost is for the $i$-th display is $c_i$. Please determine the smallest cost Maria Stepanovna should pay.


-----Input-----

The first line contains a single integer $n$ ($3 \le n \le 3\,000$) — the number of displays.

The second line contains $n$ integers $s_1, s_2, \ldots, s_n$ ($1 \le s_i \le 10^9$) — the font sizes on the displays in the order they stand along the road.

The third line contains $n$ integers $c_1, c_2, \ldots, c_n$ ($1 \le c_i \le 10^8$) — the rent costs for each display.


-----Output-----

If there are no three displays that satisfy the criteria, print -1. Otherwise print a single integer — the minimum total rent cost of three displays with indices $i < j < k$ such that $s_i < s_j < s_k$.


-----Examples-----
Input
5
2 4 5 4 10
40 30 20 10 40

Output
90

Input
3
100 101 100
2 4 5

Output
-1

Input
10
1 2 3 4 5 6 7 8 9 10
10 13 11 14 15 12 13 13 18 13

Output
33



-----Note-----

In the first example you can, for example, choose displays $1$, $4$ and $5$, because $s_1 < s_4 < s_5$ ($2 < 4 < 10$), and the rent cost is $40 + 10 + 40 = 90$.

In the second example you can't select a valid triple of indices, so the answer is -1.
"""

from math import inf

def find_minimum_rent_cost(n, s, c):
    # Initialize a 2D list to store the minimum costs for each state
    dp = [[0, inf, inf, inf] for _ in range(n)]
    
    # Base case: the first display can be the first in the sequence
    dp[0][1] = c[0]
    
    # Fill the dp table
    for j in range(1, 4):
        for i in range(1, n):
            for k in reversed(range(i)):
                if j == 1 or s[k] < s[i]:
                    dp[i][j] = min(dp[i][j], dp[k][j - 1] + c[i])
    
    # Find the minimum cost for the sequence of three displays
    result = min((x[3] for x in dp))
    
    # If the result is still inf, no valid sequence was found
    return result if result != inf else -1