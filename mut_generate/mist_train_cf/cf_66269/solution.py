"""
QUESTION:
Implement a function `pow(x, n, m)` that calculates `x` raised to the power `n` modulo `m` (i.e., `(x^n) mod m`). The input constraints are `-100.0 < x < 100.0`, `-2^31 <= n <= 2^31-1`, `1 <= m <= 1000`, and the output should satisfy `-10^4 <= (x^n) mod m <= 10^4`.
"""

def myPow(x, n, m):
    # base case
    if n == 0:
        return 1.0
    x %= m
    res = 1.0
    # if n is negative, invert x and make n positive
    if n < 0:
        x = 1 / x
        n = -n
    # binary exponentiation 
    while n:
        if n & 1:
            res = (res * x) % m
        x = (x * x) % m
        n >>= 1
    # return result modulo m, because (a * b) mod m = ((a mod m) * (b mod m)) mod m
    return res % m