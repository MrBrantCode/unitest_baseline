"""
QUESTION:
Write a function `getHappyString` that takes two integers `n` and `k` as input and returns the k-th lexicographical string of all happy strings of length `n`. A happy string is a string composed solely of letters from `['a', 'b', 'c', 'd', 'e']` where no two consecutive characters are the same. If the total number of happy strings of length `n` is less than `k`, return an empty string.

Restrictions:
- `1 <= n <= 10`
- `1 <= k <= 1000`
"""

def getHappyString(n: int, k: int) -> str:
    happy_chars = ['a', 'b', 'c']
    res = []
    def dfs(n, path):
        if n == 0:
            res.append(path)
            return 
        for char in happy_chars:
            if not path or (path and char != path[-1]):
                dfs(n - 1, path + char)
    dfs(n, "")
    return "" if k > len(res) else res[k - 1]