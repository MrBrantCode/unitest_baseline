"""
QUESTION:
You are given an array of positive integers a1, a2, ..., an × T of length n × T. We know that for any i > n it is true that ai = ai - n. Find the length of the longest non-decreasing sequence of the given array.

Input

The first line contains two space-separated integers: n, T (1 ≤ n ≤ 100, 1 ≤ T ≤ 107). The second line contains n space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 300).

Output

Print a single number — the length of a sought sequence.

Examples

Input

4 3
3 1 4 2


Output

5

Note

The array given in the sample looks like that: 3, 1, 4, 2, 3, 1, 4, 2, 3, 1, 4, 2. The elements in bold form the largest non-decreasing subsequence.
"""

def find_longest_non_decreasing_sequence_length(n, T, arr):
    if T > 2 * n:
        dp = [0] * 303
        dp1 = [0] * 303
        d = {}
        for i in range(n):
            d[arr[i]] = d.get(arr[i], 0) + 1
            for j in range(n):
                dp[arr[j]] = max(dp[arr[j]] + 1, max(dp[:arr[j]]) + 1)
        for i in range(n):
            for j in range(n - 1, -1, -1):
                dp1[arr[j]] = max(dp1[arr[j]] + 1, max(dp1[arr[j] + 1:]) + 1)
        ans = 0
        for i in range(n):
            for j in range(n):
                if arr[j] < arr[i]:
                    continue
                ans = max(ans, dp[arr[i]] + dp1[arr[j]] + (T - 2 * n) * d[arr[i]])
        return ans
    else:
        dp = [0] * 303
        for i in range(T):
            for j in range(n):
                dp[arr[j]] = max(dp[arr[j]] + 1, max(dp[:arr[j]]) + 1)
        return max(dp)