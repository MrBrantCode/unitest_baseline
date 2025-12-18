"""
QUESTION:
Implement a function Y(k) that calculates the number of positive integers n, not exceeding k, for which the polynomial Qn has at least one integer root. Qn is defined as the polynomial whose coefficients are the digits of n in reverse order.
"""

def Y(k: int) -> int:
    def Q(n: int) -> list:
        return [int(digit) for digit in str(n)[::-1]]

    count = 0
    for n in range(1, k+1):
        q = Q(n)
        degree = len(q)
        for x in range(-n, n+1):
            if sum(q[i] * x ** i for i in range(degree)) == 0:
                count += 1
                break
    return count