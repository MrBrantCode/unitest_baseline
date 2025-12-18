"""
QUESTION:
Implement the function `cut_rod(p, n)` that takes an array `p` of prices for each length of rod and an integer `n` representing the length of the rod. The function should return a tuple containing the maximum revenue that can be obtained by cutting the rod and the lengths of the pieces that yield this revenue. The time complexity of the solution should be O(n^2) and the space complexity should be O(n).
"""

def cut_rod(p, n):
    # Initialize arrays for memoization
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    
    # Reconstruct the solution
    pieces = []
    while n > 0:
        pieces.append(s[n])
        n -= s[n]
    
    return r[-1], pieces