"""
QUESTION:
Write a function `P(N)` that calculates the minimal total drag distance to arrange the cards into a single sequence in a pyramid of N cards, where the card at position `n` is `2^n mod (N+1)`, and return `P(976)`. The function should not take any arguments other than `N`.
"""

def P(N):
    def modPow(a, b, m):
        """Calculate (a^b) % m."""
        result = 1
        while b > 0:
            if b % 2 == 1:
                result = (result * a) % m
            a = (a * a) % m
            b = b // 2
        return result

    A = [(modPow(2, i, N + 1), i) for i in range(1, N + 1)]
    A.sort()
    
    inv = 0
    bit = [0] * (N + 1)
    for _, i in A:
        x = i
        while x > 0:
            inv += bit[x]
            x -= x & -x
        x = i
        while x <= N:
            bit[x] += 1
            x += x & -x

    return inv