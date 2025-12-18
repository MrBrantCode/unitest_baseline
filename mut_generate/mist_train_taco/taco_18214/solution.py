"""
QUESTION:
Poker Nim is another $2$-player game that's a simple variation on a Nim game. The rules of the games are as follows:

The game starts with $n$ piles of chips indexed from $\mbox{0}$ to $n-1$. Each pile $\boldsymbol{i}$ (where $0\leq i<n$) has $c_i$ chips.

The players move in alternating turns. During each move, the current player must perform either of the following actions:

Remove one or more chips from a single pile. 
Add one or more chips to a single pile.     

At least $\mbox{1}$ chip must be added or removed during each turn.

To ensure that the game ends in finite time, a player cannot add chips to any pile $\boldsymbol{i}$ more than $\boldsymbol{\mbox{k}}$ times.
The player who removes the last chip wins the game.

Given the values of $n$, $\boldsymbol{\mbox{k}}$, and the numbers of chips in each of the $n$ piles, determine whether the person who wins the game is the first or second person to move. Assume both players move optimally.

Input Format

The first line contains an integer, $\mathbf{T}$, denoting the number of test cases. 

Each of the $2T$ subsequent lines defines a test case. Each test case is described over the following two lines:

Two space-separated integers, $n$ (the number of piles) and $\boldsymbol{\mbox{k}}$ (the maximum number of times an individual player can add chips to some pile $\boldsymbol{i}$), respectively.
$n$ space-separated integers, $c_0,c_1,\ldots,c_{n-1}$, where each $c_i$ describes the number of chips at pile $\boldsymbol{i}$.

Constraints

$1\leq T\leq100$
$1\le n,k\le100$
$1\leq c_i\leq10^9$

Output Format

For each test case, print the name of the winner on a new line (i.e., either $\textbf{First}$ or $\textbf{Second}$).

Sample Input
2
2 5
1 2
3 5
2 1 3

Sample Output
First
Second
"""

def determine_poker_nim_winner(test_cases):
    results = []
    for case in test_cases:
        n, k, piles = case
        xor_sum = 0
        for chips in piles:
            xor_sum ^= chips
        if xor_sum == 0:
            results.append("Second")
        else:
            results.append("First")
    return results