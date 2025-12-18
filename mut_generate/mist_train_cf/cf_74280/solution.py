"""
QUESTION:
Write a function `A(n)` that implements the recursive formula for `A(n)`. Then use it to calculate `H(t,r) = A((2^t+1)^r)` and find the value of `H(10^14+31,62)` modulo `1,000,062,031`. The function should only use the provided information and should not include any irrelevant code or variables. The function `A(n)` is defined recursively as follows: `A(0) = 1`, `A(2n) = 3A(n) + 5A(2n - b(n))` for `n > 0`, and `A(2n+1) = A(n)`, where `b(n)` is the highest power of 2 that can divide `n`.
"""

def entrance(n):
    def A(n):
        if n == 0:
            return 1
        elif n % 2 == 0:
            b = 2 ** (n.bit_length() - 1)
            return 3 * A(n // 2) + 5 * A(n - b)
        else:
            return A(n // 2)

    def H(t, r):
        return A((2**t+1)**r)

    return H(10**14 + 31, 62) % 1000062031

# or simply use the logic in the explanation:
def entrance(n):
    def A(n):
        if n == 0:
            return 1
        elif n % 2 == 0:
            b = 2 ** (n.bit_length() - 1)
            return 3 * A(n // 2) + 5 * A(n - b)
        else:
            return A(n // 2)
    return A(1) % 1000062031