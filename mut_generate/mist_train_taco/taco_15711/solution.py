"""
QUESTION:
Slime and his $n$ friends are at a party. Slime has designed a game for his friends to play.

At the beginning of the game, the $i$-th player has $a_i$ biscuits. At each second, Slime will choose a biscuit randomly uniformly among all $a_1 + a_2 + \ldots + a_n$ biscuits, and the owner of this biscuit will give it to a random uniform player among $n-1$ players except himself. The game stops when one person will have all the biscuits.

As the host of the party, Slime wants to know the expected value of the time that the game will last, to hold the next activity on time.

For convenience, as the answer can be represented as a rational number $\frac{p}{q}$ for coprime $p$ and $q$, you need to find the value of $(p \cdot q^{-1})\mod 998\,244\,353$. You can prove that $q\mod 998\,244\,353 \neq 0$.


-----Input-----

The first line contains one integer $n\ (2\le n\le 100\,000)$: the number of people playing the game.

The second line contains $n$ non-negative integers $a_1,a_2,\dots,a_n\ (1\le a_1+a_2+\dots+a_n\le 300\,000)$, where $a_i$ represents the number of biscuits the $i$-th person own at the beginning.


-----Output-----

Print one integer: the expected value of the time that the game will last, modulo $998\,244\,353$.


-----Examples-----
Input
2
1 1

Output
1

Input
2
1 2

Output
3

Input
5
0 0 0 0 35

Output
0

Input
5
8 4 2 0 1

Output
801604029



-----Note-----

For the first example, in the first second, the probability that player $1$ will give the player $2$ a biscuit is $\frac{1}{2}$, and the probability that player $2$ will give the player $1$ a biscuit is $\frac{1}{2}$. But anyway, the game will stop after exactly $1$ second because only one player will occupy all biscuits after $1$ second, so the answer is $1$.
"""

import math

def calculate_expected_game_time(n, a, mod=998244353):
    def inv(x):
        return pow(x, mod - 2, mod)
    
    tot = sum(a)
    dp = [[0, 0] for _ in range(tot + 1)]
    
    dp[0] = [0, 1]
    dp[1] = [(1 - n + mod) % mod, 1]
    
    for k in range(1, tot):
        temp = inv(tot - k)
        dp[k + 1][0] = -tot * (n - 1) - dp[k][0] * (2 * k - tot - k * n) - dp[k - 1][0] * k * (n - 1)
        dp[k + 1][0] *= temp
        dp[k + 1][0] = (dp[k + 1][0] % mod + mod) % mod
        dp[k + 1][1] = -dp[k][1] * (2 * k - tot - k * n) - dp[k - 1][1] * k * (n - 1)
        dp[k + 1][1] *= temp
        dp[k + 1][1] = (dp[k + 1][1] % mod + mod) % mod
    
    alpha = -dp[tot][0] * inv(dp[tot][1])
    alpha = (alpha % mod + mod) % mod
    
    ans = 0
    for i in range(n):
        ans += dp[a[i]][0] + dp[a[i]][1] * alpha
        ans = (ans % mod + mod) % mod
    
    ans -= alpha * (n - 1)
    ans = (ans % mod + mod) % mod
    ans *= inv(n)
    ans = (ans % mod + mod) % mod
    
    return ans