"""
QUESTION:
Read problems statements [Bengali] and [Vietnamese] as well.

Ghayeeth is a math teacher. He likes playing games, so he invented a new game which he wants to play against his student Siroj. The rules of the game are as follows:
Initially, Ghayeeth writes the numbers  $A_{1}, A_{2}, \dots, A_{N}$ on a whiteboard and a number $Z=0$ on a piece of paper.
Ghayeeth and Siroj alternate turns; Ghayeeth goes first.
In each turn, the current player must pick a number that is currently written on the whiteboard, add it to $Z$ and erase it from the whiteboard.
After each turn, if there is no pair of positive integers $(a, b)$ such that $Z = a^{2} - b^{2}$, then the last player who made a move loses the game.
Otherwise, if there are no more numbers on the whiteboard, the last player who made a move wins the game.

Help Ghayeeth determine the winner of this game.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
The second line contains $N$ space-separated integers $A_{1}, A_{2}, \dots, A_{N}$.

------  Output ------
For each test case, print a single line containing the string "Ghayeeth" or "Siroj" (without quotes) — the name of the winner.

------  Constraints  ------
$1 ≤ T ≤ 10$
$1 ≤ N ≤ 300$
$5 ≤ A_{i} ≤ 100,000$ for each valid $i$

----- Sample Input 1 ------ 
2
3
7 9 11
2
13 15
----- Sample Output 1 ------ 
Ghayeeth
Siroj
"""

from collections import Counter

def determine_winner(test_cases):
    def grundy(state, g):
        if g in gdic:
            return gdic[g]
        subg = set()
        if g[0] > 0:
            subg.add(grundy(state, tuple((g[0] - 1, g[1], g[2], g[3]))))
        if g[1] > 0 and state != 1:
            subg.add(grundy((state + 1) % 4, tuple((g[0], g[1] - 1, g[2], g[3]))))
        if g[2] > 0 and state != 0:
            subg.add(grundy((state + 2) % 4, tuple((g[0], g[1], g[2] - 1, g[3]))))
        if g[3] > 0 and state != 3:
            subg.add(grundy((state + 3) % 4, tuple((g[0], g[1], g[2], g[3] - 1))))
        if len(subg) == 0:
            gdic[g] = 0
        else:
            mex = 0
            while mex in subg:
                mex += 1
            gdic[g] = mex
        return gdic[g]

    res = ('Ghayeeth', 'Siroj')
    winners = []

    for n, A in test_cases:
        vals = Counter((int(z) % 4 for z in A))
        st = tuple((vals[0] % 2, vals[1], vals[2] % 2, vals[3]))
        gdic = dict()
        winners.append(res[grundy(0, st) == 0])

    return winners