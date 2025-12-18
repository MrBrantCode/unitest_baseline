"""
QUESTION:
Genos recently installed the game Zuma on his phone. In Zuma there exists a line of n gemstones, the i-th of which has color ci. The goal of the game is to destroy all the gemstones in the line as quickly as possible.

In one second, Genos is able to choose exactly one continuous substring of colored gemstones that is a palindrome and remove it from the line. After the substring is removed, the remaining gemstones shift to form a solid line again. What is the minimum number of seconds needed to destroy the entire line?

Let us remind, that the string (or substring) is called palindrome, if it reads same backwards or forward. In our case this means the color of the first gemstone is equal to the color of the last one, the color of the second gemstone is equal to the color of the next to last and so on.

Input

The first line of input contains a single integer n (1 ≤ n ≤ 500) — the number of gemstones.

The second line contains n space-separated integers, the i-th of which is ci (1 ≤ ci ≤ n) — the color of the i-th gemstone in a line.

Output

Print a single integer — the minimum number of seconds needed to destroy the entire line.

Examples

Input

3
1 2 1


Output

1


Input

3
1 2 3


Output

3


Input

7
1 4 4 2 3 2 1


Output

2

Note

In the first sample, Genos can destroy the entire line in one second.

In the second sample, Genos can only destroy one gemstone at a time, so destroying three gemstones takes three seconds.

In the third sample, to achieve the optimal time of two seconds, destroy palindrome 4 4 first and then destroy palindrome 1 2 3 2 1.
"""

def min_seconds_to_destroy_gemstones(n, s):
    """
    Calculate the minimum number of seconds needed to destroy the entire line of gemstones.

    Parameters:
    n (int): The number of gemstones.
    s (list of int): A list of integers representing the colors of the gemstones.

    Returns:
    int: The minimum number of seconds needed to destroy the entire line of gemstones.
    """
    dp = [[-1 for _ in range(501)] for _ in range(500)]

    def sol(i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        if dp[i][j] != -1:
            return dp[i][j]
        x = 502
        if s[i] == s[i + 1]:
            x = min(x, sol(i + 2, j) + 1)
        for k in range(i + 2, j + 1):
            if s[i] == s[k]:
                x = min(x, sol(i + 1, k - 1) + sol(k + 1, j))
        dp[i][j] = min(1 + sol(i + 1, j), x)
        return dp[i][j]

    return sol(0, n - 1)