"""
QUESTION:
Write a function `getHappyString(n: int, k: int) -> str` to find the k-th lexicographical string of all happy strings of length `n`. A happy string is a string composed solely of letters 'a', 'b', 'c' where `s[i] != s[i + 1]` for all values of `i` ranging from `1` to `s.length - 1`. If the total number of happy strings of length `n` is less than `k`, return an empty string. The constraints are `1 <= n <= 10` and `1 <= k <= 100`.
"""

def getHappyString(n: int, k: int) -> str:
    ans = []
    def dfs(s):
        if len(s) == n:
            ans.append(s)
        elif len(s) < n:
            for c in 'abc':
                if len(s) == 0 or (len(s) > 0 and s[-1] != c):
                    dfs(s + c)

    dfs('')
    
    return ans[k - 1] if k - 1 < len(ans) else ''