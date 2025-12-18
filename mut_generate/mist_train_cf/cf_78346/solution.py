"""
QUESTION:
Write a function `binomial_coefficient(n, m)` that calculates the binomial coefficient for given numbers `n` and `m` where `m <= n`. The function should handle large inputs efficiently using memoization and manage potential memory overflow errors.
"""

def binomial_coefficient(n, m):
    # Create an empty 2D table with (n+1) rows and (n+1) columns.
    C = [[0 for x in range(n+1)] for x in range(n+1)]

    try:
        # Calculate binomial coefficient in bottom-up manner.
        for i in range(n+1):
            for j in range(min(i, m)+1):
                # Base cases: when m=0 or m=n, the coefficient is 1.
                if j == 0 or j == i:
                    C[i][j] = 1
                # Use the recursive formula: C(n, m) = C(n-1, m-1) + C(n-1, m).
                else:
                    C[i][j] = C[i-1][j-1] + C[i-1][j]

    except MemoryError:
        print("Memory Overflow Exception Caught!")
        return
    
    return C[n][m]