"""
QUESTION:
Implement the function `cutBar(m, n)` which calculates the minimum number of cuts required to cut a bar of length `n` into pieces. The cutting rule is as follows: 
- If the current length is less than `m`, double the length in the next cut.
- If the current length is greater than or equal to `m`, increase the length by `m` in the next cut.
- The cutting process is complete when the current length is greater than or equal to `n`.
- Both `m` and `n` are positive integers, and `m` is less than or equal to `n`.
"""

def cutBar(m, n):
    def cutBarDFS(now):
        if now >= n:
            return 0
        if now < m:
            return 1 + cutBarDFS(now * 2)
        return 1 + cutBarDFS(now + m)
    return cutBarDFS(1)