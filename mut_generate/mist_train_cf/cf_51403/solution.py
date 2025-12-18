"""
QUESTION:
Write a function `superEggDrop` that takes two integers `k` and `n` as input and returns the minimum number of moves required to determine with certainty the value of `f` where `0 <= f <= n`, given `k` identical eggs and a building with `n` floors labeled from `1` to `n`. Each move, you may take an unbroken egg and drop it from any floor `x` (where `1 <= x <= n`). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves. 

Constraints:
`1 <= k <= 100`
`1 <= n <= 104`
"""

def superEggDrop(k: int, n: int) -> int:
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    
    for m in range(1, n+1):
        for i in range(1, k+1):
            low, high = 1, n
            
            while low <= high:
                mid = (low + high) // 2
                left, right = dp[i-1][mid-1], dp[i][n-mid]
                
                if left < right:
                    low = mid + 1
                    dp[i][m] = left + 1
                elif left > right:
                    high = mid - 1
                    dp[i][m] = right + 1
                else:
                    dp[i][m] = left + 1
                    low = mid + 1
                    
            if dp[i][m] >= n:
                return m
    return n