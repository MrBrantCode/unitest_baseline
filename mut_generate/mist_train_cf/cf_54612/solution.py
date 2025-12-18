"""
QUESTION:
Define a function F(N) that counts the number of quintuples (a, b, c, e, f) that satisfy the equation a^e+b^e=c^f, where 0 < a < b, e >= 2, f >= 3, and c^f <= N.
"""

def F(N):
    from math import pow
    result = 0
    c_limit = int(N ** (1/3)) + 1
    for c in range(1, c_limit):
        for f in range(3, 21):
            if pow(c, f) > N:
                break
            a = 1
            b = c - 1
            while a < b:
                temp = pow(a, 2) + pow(b, 2)
                c_pow = pow(c, f)
                if temp == c_pow:
                    result += 1
                    a += 1
                    b -= 1
                elif temp < c_pow:
                    a += 1
                else:
                    b -= 1
    return result