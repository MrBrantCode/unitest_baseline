"""
QUESTION:
Given an integer array `arr` and an integer `k`, write a function `odd_even_jump(arr, k)` that returns the number of good starting indices such that the total number of jumps made from that index is exactly `k`. A starting index is good if, starting from that index, you can reach the end of the array by jumping some number of times, where jumps are made according to the following rules:
- During odd-numbered jumps, you jump to the index `j` such that `arr[i] <= arr[j]` and `arr[j]` is the smallest possible value.
- During even-numbered jumps, you jump to the index `j` such that `arr[i] >= arr[j]` and `arr[j]` is the largest possible value.
Constraints: 
- `1 <= arr.length <= 2 * 10^4`
- `0 <= arr[i] <= 10^5`
- `1 <= k <= arr.length`
"""

def odd_even_jump(arr, k):
    n = len(arr)
    index = sorted(range(n), key = lambda i: (-arr[i], -i))
    oddNext = [None] * n
    evenNext = [None] * n
    stack = []
    for i in index:
        while stack and stack[-1] < i:
            oddNext[stack.pop()] = i
        stack.append(i)
    stack = []
    for i in index[::-1]:
        while stack and stack[-1] < i:
            evenNext[stack.pop()] = i
        stack.append(i)
    dp = [[False]*(k+1) for _ in range(n)]
    dp[-1] = [True]*(k+1)
    for i in range(n-2, -1, -1):
        if oddNext[i] is not None:
            dp[i][1] = dp[oddNext[i]][0]
            for j in range(2,k+1):
                if evenNext[i] is not None:
                    dp[i][j] = dp[oddNext[i]][j-1] or dp[evenNext[i]][j-1]
    return sum(dp[i][k] for i in range(n))