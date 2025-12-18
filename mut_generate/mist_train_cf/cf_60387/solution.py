"""
QUESTION:
Write a function `convergent(n)` that takes an integer `n` as input and returns the sum of digits in the numerator of the nth convergent of the continued fraction for `e`. The continued fraction for `e` is `[2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ... , 1, 2k, 1, ...]`. The function should use the recursion formulae for a general continued fraction convergent: `P[-1] = 1, P[-2] = 0, P[n] = an*P[n-1] + P[n-2]` and `Q[-1] = 0, Q[-2] = 1, Q[n] = an*Q[n-1] + Q[n-2]`.
"""

def convergent(n):
    sequence = [2]
    k = 1
    while len(sequence) < n:
        sequence += [1,2*k,1]
        k += 1
    P = [0, 1]
    Q = [1, 0]
    for a in sequence:
        P.append(a*P[-1] + P[-2])
        Q.append(a*Q[-1] + Q[-2])
    numerator = P[-1]
    numerator_digits = [int(d) for d in str(numerator)]
    return sum(numerator_digits)