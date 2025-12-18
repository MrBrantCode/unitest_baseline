"""
QUESTION:
Compute the function f(n, k) which represents the count of winning scenarios for the initial player in a game with k heaps of stones, each containing between 2 and n stones. The game ends when a player is unable to make a valid move, resulting in their loss. A valid move is to select a heap and substitute it with two new heaps of stones, where the quantity of stones in both new heaps must exceed one but be less than the quantity in the original heap, and the quantity of stones in each new heap must be a factor of the quantity in the original heap.

The function f(n, k) should be computed modulo 987654321.
"""

def entance(n, k):
    mod = 987654321
    factorCount = [1 for _ in range(n + 1)]
    primePowerCount = [1 for _ in range(n + 1)]
    for p in range(2, n + 1):
        if factorCount[p] == 1:  
            primePowerCount[p], q = 2, p * p
            while q <= n:
                primePowerCount[q] += 1
                q *= p
        for multiple in range(2 * p, n + 1, p):
            factorCount[multiple] += factorCount[p]
    sumCount = [0 for _ in range(n + 1)]
    for value in range(2, n + 1):
        sumCount[value] = (sumCount[value - 1] + primePowerCount[value] * factorCount[value]) % mod
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    for _ in range(k):
        for value in range(n, 0, -1):
            dp[value] = (dp[value] + dp[value - 1] * sumCount[value]) % mod
    return dp[n]