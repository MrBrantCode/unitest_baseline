"""
QUESTION:
This time around, Baby Ehab will play with permutations. He has $n$ cubes arranged in a row, with numbers from $1$ to $n$ written on them. He'll make exactly $j$ operations. In each operation, he'll pick up $2$ cubes and switch their positions.

He's wondering: how many different sequences of cubes can I have at the end? Since Baby Ehab is a turbulent person, he doesn't know how many operations he'll make, so he wants the answer for every possible $j$ between $1$ and $k$.


-----Input-----

The only line contains $2$ integers $n$ and $k$ ($2 \le n \le 10^9$, $1 \le k \le 200$) — the number of cubes Baby Ehab has, and the parameter $k$ from the statement.


-----Output-----

Print $k$ space-separated integers. The $i$-th of them is the number of possible sequences you can end up with if you do exactly $i$ operations. Since this number can be very large, print the remainder when it's divided by $10^9+7$.


-----Examples-----

Input
2 3
Output
1 1 1
Input
3 2
Output
3 3
Input
4 2
Output
6 12


-----Note-----

In the second example, there are $3$ sequences he can get after $1$ swap, because there are $3$ pairs of cubes he can swap. Also, there are $3$ sequences he can get after $2$ swaps:

$[1,2,3]$,

$[3,1,2]$,

$[2,3,1]$.
"""

def calculate_possible_sequences(n: int, k: int) -> list[int]:
    mod = 1000000007
    
    # Calculate Binomial Coefficients
    BC = [1] * (2 * k + 1)
    for i in range(1, 2 * k + 1):
        BC[i] = BC[i - 1] * (n - i + 1) * pow(i, mod - 2, mod) % mod
    
    # Calculate Stirling Numbers of the Second Kind
    S = [[0] * k for _ in range(2 * k - 1)]
    S[0][0] = 1
    for i in range(1, 2 * k - 1):
        for j in range(1 + i // 2):
            S[i][j] = (i + 1) * S[i - 1][j]
            if j:
                S[i][j] += (i + 1) * S[i - 2][j - 1]
            S[i][j] %= mod
    
    # Calculate the number of possible sequences
    DP = [1] * (k + 1)
    DP[1] = n * (n - 1) // 2 % mod
    for i in range(2, k + 1):
        DP[i] = DP[i - 2]
        for t in range(1, i + 1):
            value = S[i + t - 2][t - 1] * BC[i + t] % mod
            DP[i] += value
            DP[i] %= mod
    
    return DP[1:]