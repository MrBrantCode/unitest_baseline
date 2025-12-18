"""
QUESTION:
Calculate the sum of all composite integers $1 \lt n \le 2 \times 10^{11}$, for which the coresilience $C(n)$ is a unit fraction. The function `sum_of_composites(limit)` should take an integer `limit` as input and return the sum of all composite integers less than or equal to `limit` that satisfy the condition. Note that the limit will be $2 \times 10^{11}$.
"""

def euler_totient(n):
    result = n 
    p = 2
    while p * p <= n: 
        if n % p: 
            p += 1
        else: 
            while (n % p) == 0: 
                n //= p 
            result -= result // p
    if n > 1: result -= result // n 
    return result

def sum_of_composites(limit):
    sum_of_nums = 0
    for x in range(2, int(limit**0.5)+1):
        y = x
        while y < limit:
            if euler_totient(y) == y - x:
                sum_of_nums += y
            y *= x
    return sum_of_nums