"""
QUESTION:
Write a function `least_fibonacci(k)` that determines the least quantity of Fibonacci figures whose aggregate equals `k`, where the same Fibonacci figure can be utilized multiple times. The Fibonacci figures are defined as follows: `F1 = 1`, `F2 = 1`, and `Fn = Fn-1 + Fn-2` for `n > 2`. The function should take an integer `k` as input where `1 <= k <= 10^9`.
"""

def least_fibonacci(k):
    fibs = [1, 1]
    while fibs[-1] <= k: 
        fibs.append(fibs[-1] + fibs[-2]) 
    count = 0
    idx = len(fibs) - 1
    while k: 
        if fibs[idx] <= k: 
            k -= fibs[idx] 
            count += 1
        idx -= 1
    return count