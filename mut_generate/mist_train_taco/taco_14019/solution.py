"""
QUESTION:
You are given an array a with n elements. Each element of a is either 0 or 1.

Let's denote the length of the longest subsegment of consecutive elements in a, consisting of only numbers one, as f(a). You can change no more than k zeroes to ones to maximize f(a).


-----Input-----

The first line contains two integers n and k (1 ≤ n ≤ 3·10^5, 0 ≤ k ≤ n) — the number of elements in a and the parameter k.

The second line contains n integers a_{i} (0 ≤ a_{i} ≤ 1) — the elements of a.


-----Output-----

On the first line print a non-negative integer z — the maximal value of f(a) after no more than k changes of zeroes to ones.

On the second line print n integers a_{j} — the elements of the array a after the changes.

If there are multiple answers, you can print any one of them.


-----Examples-----
Input
7 1
1 0 0 1 1 0 1

Output
4
1 0 0 1 1 1 1

Input
10 2
1 0 0 1 0 1 0 1 0 1

Output
5
1 0 0 1 1 1 1 1 0 1
"""

import bisect

def maximize_consecutive_ones(a, k):
    n = len(a)
    dp = [0] * (n + 1)
    
    # Calculate the prefix sum of zeroes
    for i in range(n):
        if a[i] == 0:
            dp[i + 1] += 1
        dp[i + 1] += dp[i]
    
    maxi = -1
    ind = -1
    
    # Find the maximum length of subsegment of consecutive ones
    for i in range(1, len(dp)):
        ans = bisect.bisect_left(dp, dp[i] - k)
        maxi = max(maxi, i - ans)
        if maxi == i - ans:
            ind = i
    
    # Modify the array to reflect the changes
    end = ind - 1
    strt = end - maxi + 1
    modified_array = a[:]
    for i in range(strt, end + 1):
        modified_array[i] = 1
    
    return maxi, modified_array