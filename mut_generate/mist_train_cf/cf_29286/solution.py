"""
QUESTION:
Implement a function `modular_inverse(a, m)` that takes two integers `a` and `m` as input and returns the modular inverse of `a` modulo `m` using the extended Euclidean algorithm. The function should return `None` if the modular inverse does not exist, i.e., when `a` and `m` are not coprime. The output should be an integer `x` such that `(a * x) % m = 1`.
"""

def modular_inverse(a, m):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = egcd(b % a, a)
            return (g, y - (b // a) * x, x)

    g, x, y = egcd(a, m)
    if g != 1:
        return None  
    else:
        return x % m