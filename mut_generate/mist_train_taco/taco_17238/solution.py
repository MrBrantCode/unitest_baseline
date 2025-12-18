"""
QUESTION:
We'll call an array of n non-negative integers a[1], a[2], ..., a[n] interesting, if it meets m constraints. The i-th of the m constraints consists of three integers li, ri, qi (1 ≤ li ≤ ri ≤ n) meaning that value <image> should be equal to qi. 

Your task is to find any interesting array of n elements or state that such array doesn't exist.

Expression x&y means the bitwise AND of numbers x and y. In programming languages C++, Java and Python this operation is represented as "&", in Pascal — as "and".

Input

The first line contains two integers n, m (1 ≤ n ≤ 105, 1 ≤ m ≤ 105) — the number of elements in the array and the number of limits.

Each of the next m lines contains three integers li, ri, qi (1 ≤ li ≤ ri ≤ n, 0 ≤ qi < 230) describing the i-th limit.

Output

If the interesting array exists, in the first line print "YES" (without the quotes) and in the second line print n integers a[1], a[2], ..., a[n] (0 ≤ a[i] < 230) decribing the interesting array. If there are multiple answers, print any of them.

If the interesting array doesn't exist, print "NO" (without the quotes) in the single line.

Examples

Input

3 1
1 3 3


Output

YES
3 3 3


Input

3 2
1 3 3
1 3 2


Output

NO
"""

def find_interesting_array(n, m, constraints):
    dp = [[0] * 30 for _ in range(n + 2)]
    
    for (l, r, q) in constraints:
        mask = 1
        cou = 29
        while mask <= q:
            if mask & q:
                dp[l][cou] += 1
                dp[r + 1][cou] -= 1
            cou -= 1
            mask <<= 1
    
    ans = [[0] * 30 for _ in range(n)]
    for i in range(30):
        a = 0
        for j in range(n):
            a += dp[j + 1][i]
            dp[j + 1][i] = dp[j][i]
            if a:
                ans[j][i] = 1
                dp[j + 1][i] += 1
    
    for (l, r, q) in constraints:
        mask = 1
        for cou in range(29, -1, -1):
            if not mask & q and dp[r][cou] - dp[l - 1][cou] == r - l + 1:
                return ("NO",)
            mask <<= 1
    
    interesting_array = [int(''.join(map(str, ans[i])), 2) for i in range(n)]
    return ("YES", interesting_array)