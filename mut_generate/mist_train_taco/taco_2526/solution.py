"""
QUESTION:
Two players (numbered $\mbox{1}$ and $2$) are playing a game of Tower Breakers! The rules of the game are as follows:

Player $\mbox{1}$ always moves first.
Initially there are $N$ towers of various heights.
The players move in alternating turns. In each turn, a player must choose a tower of height $\mbox{X}$ and break it down into $\mathbf{Y}$ towers, each of height $\mbox{z}$. The numbers $\mathbf{Y}$ and $\mbox{z}$ must satisfy $Y\times Z=X$ and $Y>1$.  
If the current player is unable to make any move, they lose the game.

Given the value of $N$ and the respective height values for all towers, can you determine who will win, assuming both players always move optimally? If the first player wins, print $\mbox{1}$; otherwise, print $2$.

Input Format

The first line contains an integer, $\mathbf{T}$, denoting the number of test cases. 

The $2T$ subsequent lines define the test cases. Each test case is described by two lines:

An integer, $N$, denoting the number of towers.
$N$ space-separated integers, $h_0,h_1,\ldots,h_{N-1}$, where each $h_i$ describes the height of tower $\boldsymbol{i}$.

Constraints

$1\leq T\leq200$
$1\leq N\leq100$
$1\leq h_i\leq10^5$

Output Format

For each test case, print a single integer denoting the winner (i.e., either $\mbox{1}$ or $2$) on a new line.

Sample Input
2
2 
1 2
3 
1 2 3

Sample Output
1
2

Explanation

In the first test case, the first player simply breaks down the second tower of height $2$ into two towers of height $\mbox{1}$ and wins.

In the second test case, there are only two possible moves:

Break the second tower into $2$ towers of height $\mbox{1}$.
Break the third tower into $3$ towers of height $\mbox{1}$. 

Whichever move player $\mbox{1}$ makes, player $2$ can make the other move and win the game.
"""

from functools import reduce

def mex(s):
    f = 0
    m = max(s)
    for i in range(m):
        if i not in s:
            return i
    return m + 1

def factors(n):
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))

def grundy(n):
    if n in [0, 1]:
        return 0
    s = {0}
    f = factors(n) - {1, n}
    for e in f:
        if e % 2 == 1:
            s.add(grundy(int(n / e)))
    return mex(s)

def determine_winner(test_cases):
    results = []
    for n, heights in test_cases:
        g = grundy(heights[0])
        for i in range(1, n):
            g ^= grundy(heights[i])
        if g == 0:
            results.append(2)
        else:
            results.append(1)
    return results