"""
QUESTION:
You are given an array $a$ consisting of $n$ integers. Beauty of array is the maximum sum of some consecutive subarray of this array (this subarray may be empty). For example, the beauty of the array [10, -5, 10, -4, 1] is 15, and the beauty of the array [-3, -5, -1] is 0.

You may choose at most one consecutive subarray of $a$ and multiply all values contained in this subarray by $x$. You want to maximize the beauty of array after applying at most one such operation.


-----Input-----

The first line contains two integers $n$ and $x$ ($1 \le n \le 3 \cdot 10^5, -100 \le x \le 100$) — the length of array $a$ and the integer $x$ respectively.

The second line contains $n$ integers $a_1, a_2, \dots, a_n$ ($-10^9 \le a_i \le 10^9$) — the array $a$.


-----Output-----

Print one integer — the maximum possible beauty of array $a$ after multiplying all values belonging to some consecutive subarray $x$.


-----Examples-----
Input
5 -2
-3 8 -2 1 -6

Output
22

Input
12 -3
1 3 3 7 1 3 3 7 1 3 3 7

Output
42

Input
5 10
-1 -2 -3 -4 -5

Output
0



-----Note-----

In the first test case we need to multiply the subarray [-2, 1, -6], and the array becomes [-3, 8, 4, -2, 12] with beauty 22 ([-3, 8, 4, -2, 12]).

In the second test case we don't need to multiply any subarray at all.

In the third test case no matter which subarray we multiply, the beauty of array will be equal to 0.
"""

def maximize_array_beauty(n, x, a):
    # Initialize the dp array with zeros
    dp = [[0, 0, 0] for _ in range(n + 1)]
    ma = 0  # Initialize the maximum beauty to 0

    for i in range(1, n + 1):
        dp[i][0] = max(dp[i - 1][0] + a[i - 1], 0)
        dp[i][1] = max(dp[i - 1][1] + a[i - 1] * x, dp[i - 1][0] + a[i - 1] * x)
        dp[i][2] = max(dp[i - 1][2] + a[i - 1], a[i - 1] + dp[i - 1][1])
        ma = max(dp[i][0], dp[i][1], dp[i][2], ma)

    return ma