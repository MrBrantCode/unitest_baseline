"""
QUESTION:
Implement the `fibfib` function to efficiently compute the n-th element of the FibFib number sequence. The FibFib sequence is defined as: `fibfib(0) == 0`, `fibfib(1) == 0`, `fibfib(2) == 1`, and `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)` for `n > 2`. Use dynamic programming to optimize the function.
"""

def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        memo = [0] * (n+1)
        memo[0] = 0
        memo[1] = 0
        memo[2] = 1

        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        
        return memo[n]