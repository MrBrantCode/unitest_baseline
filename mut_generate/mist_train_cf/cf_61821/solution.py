"""
QUESTION:
You are given `n` pairs of numbers where the first number is always smaller than the second number. A pair `(c, d)` can follow another pair `(a, b)` if and only if `b < c`. The task is to find the length of the longest chain which can be formed by selecting pairs in any order such that the sum of all first elements in the pairs is an even number. The function `findLongestChain(pairs)` should take a list of pairs as input and return the length of the longest chain. The number of given pairs will be in the range [1, 1000] and the first element of each pair will be in the range [1, 10000].
"""

def findLongestChain(pairs):
    pairs.sort(key=lambda x: x[1])
    n = len(pairs)
    dp = [1] * n
    maxLen = 1
    for i in range(1, n):
        for j in range(i):
            if pairs[i][0] > pairs[j][1] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
        maxLen = max(maxLen, dp[i])

    for i in range(n - 1, -1, -1):
        if pairs[i][0] % 2 == 0:
            return maxLen
        else:
            for j in range(i - 1, -1, -1):
                if pairs[j][0] % 2 == 0:
                    maxLen = max(maxLen, dp[j] + 1 if (pairs[i][0] + pairs[j][0]) % 2 == 0 else dp[j])
                    break
    return maxLen