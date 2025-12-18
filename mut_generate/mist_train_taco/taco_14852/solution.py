"""
QUESTION:
Stephanie just learned about a game called Nim in which there are two players and $n$ piles of stones. During each turn, a player must choose any non-empty pile and take as many stones as they want. The first player who cannot complete their turn (i.e., because all piles are empty) loses.  

Stephanie knows that, for each start position in this game, it's possible to know which player will win (i.e., the first or second player) if both players play optimally. Now she wants to know the number of different games that exist that satisfy all of the following conditions:

The game starts with $n$ non-empty piles and each pile contains less than $2^{m}$ stones.
All the piles contain pairwise different numbers of stones.
The first player wins if that player moves optimally.

Help Stephanie by finding and printing the number of such games satisfying all the above criteria, modulo $10^9+7$.

Input Format

The first line contains two space-separated integers describing the respective values of $n$ and $m$.

Constraints

$1\leq n,m\leq10^7$  

Output Format

Print the number of such games, modulo $10^9+7$.

Sample Input 0
2 2

Sample Output 0
6

Explanation 0

We want to know the number of games with $n=2$ piles where each pile contains $<2^m=2^2=4$ stones. There are six such possible games with the following distributions of stones: $(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)$. Thus, we print the result of $6\ \text{mod}\ (10^9+7)=6$ as our answer.
"""

def count_winning_nim_games(n: int, m: int) -> int:
    mod = 10**9 + 7
    M = pow(2, m, mod) - 1
    
    if n == 1:
        return M % mod
    elif n == 2:
        return (M * (M - 1)) % mod
    
    comb_n_1 = M * (M - 1) % mod
    nim_n_2 = 0
    nim_n_1 = 0
    nim_n = 0
    
    for i in range(3, n + 1):
        nim_n = (comb_n_1 - nim_n_1 - nim_n_2 * (M - i + 2) * (i - 1)) % mod
        comb_n_1 = comb_n_1 * (M - i + 1) % mod
        nim_n_2 = nim_n_1
        nim_n_1 = nim_n
    
    return (comb_n_1 - nim_n) % mod