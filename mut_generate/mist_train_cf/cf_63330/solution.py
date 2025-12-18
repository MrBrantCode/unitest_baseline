"""
QUESTION:
Write a function `numOfWays(words, target, n)` that takes in a list of strings `words`, a string `target`, and an integer `n` as input. The function should return the number of ways to form `target` using the given `words` under certain rules, modulo `10^9 + 7`.

The rules are as follows:
- `target` should be formed from left to right.
- To form the `ith` character of `target`, you can choose the `kth` character of the `jth` string in `words` if `target[i] = words[j][k]`.
- Once you use the `kth` character of the `jth` string of `words`, you can no longer use the `xth` character of any string in `words` where `x <= k`.
- Each string in `words` can only be used once.
- The total number of characters used from all strings in `words` to form `target` should not exceed `n`.

Constraints:
- `1 <= len(words) <= 1000`
- `1 <= len(words[i]) <= 1000`
- All strings in `words` have the same length.
- `1 <= len(target) <= 1000`
- `words[i]` and `target` contain only lowercase English letters.
- `1 <= n <= 1000`
"""

def numOfWays(words, target, n):
    mod = 10**9+7
    m=len(words)
    l=len(words[0])
    t=len(target)

    count=[[0]*26 for _ in range(l)]
    for word in words:
        for i in range(l):
            count[i][ord(word[i])-97]+=1
            
    dp, nxt = [[0]*(n+1) for _ in range(t+1)], [[0]*(n+1) for _ in range(t+1)]
    dp[0][0]=1
    for i in range(1,t+1):
        for k in range(i,min(n,i*l)+1):
            for c in range(m):
                if k-c-1>=0:
                    nxt[i][k]=(nxt[i][k]+nxt[i][k-c-1]*count[c-1][ord(target[i-1])-97])%mod
            dp[i][k] = (dp[i-1][k-1]+nxt[i][k]) % mod
            
    return dp[t][n]