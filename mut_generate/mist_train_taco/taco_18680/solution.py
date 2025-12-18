"""
QUESTION:
Takahashi throws N dice, each having K sides with all integers from 1 to K. The dice are NOT pairwise distinguishable.
For each i=2,3,...,2K, find the following value modulo 998244353:
 - The number of combinations of N sides shown by the dice such that the sum of no two different sides is i.
Note that the dice are NOT distinguishable, that is, two combinations are considered different when there exists an integer k such that the number of dice showing k is different in those two.

-----Constraints-----
 - 1 \leq K \leq 2000
 - 2 \leq N \leq 2000
 - K and N are integers.

-----Input-----
Input is given from Standard Input in the following format:
K N

-----Output-----
Print 2K-1 integers. The t-th of them (1\leq t\leq 2K-1) should be the answer for i=t+1.

-----Sample Input-----
3 3

-----Sample Output-----
7
7
4
7
7

 - For i=2, the combinations (1,2,2),(1,2,3),(1,3,3),(2,2,2),(2,2,3),(2,3,3),(3,3,3) satisfy the condition, so the answer is 7.
 - For i=3, the combinations (1,1,1),(1,1,3),(1,3,3),(2,2,2),(2,2,3),(2,3,3),(3,3,3) satisfy the condition, so the answer is 7.
 - For i=4, the combinations (1,1,1),(1,1,2),(2,3,3),(3,3,3) satisfy the condition, so the answer is 4.
"""

def count_valid_dice_combinations(k, n):
    def cmb(n, r):
        if n < 0:
            return 0
        if n == 0:
            if r != 0:
                return 0
            else:
                return 1
        elif r < 0:
            return 0
        elif r > n:
            return 0
        elif r == 0:
            return 1
        elif r == n:
            return 1
        else:
            return A[n] * B[r] * B[n - r] % mod

    mod = 998244353
    A = [1, 1]
    B = [1, 1]
    for i in range(2, 4005):
        A.append(A[-1] * i % mod)
        B.append(B[-1] * pow(i, mod - 2, mod) % mod)

    if k == 1:
        return [0] * (2 * k - 1)

    ans = [0] * (2 * k + 1)
    for i in range(2, k + 3):
        if i % 2 == 0:
            i = i + 1
            for j in range(min(n + 1, i // 2 + 1)):
                ans[i - 1] = (ans[i - 1] + cmb(n + k - i, k - i + j) * cmb(i // 2, j) * pow(2, j, mod)) % mod
        else:
            ans[i] = ans[i - 1]

    for i in range(k + 2, 2 * k + 1):
        ans[i] = ans[2 * k + 2 - i]

    return ans[2:2 * k + 1]