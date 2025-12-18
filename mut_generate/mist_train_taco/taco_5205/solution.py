"""
QUESTION:
# Task
 Mobius function - an important function in number theory. For each given n, it only has 3 values:
```
0  -- if n divisible by square of a prime. Such as: 4, 8, 9
1  -- if n not divisible by any square of a prime 
        and have even number of prime factor. Such as: 6, 10, 21
-1 -- otherwise. Such as: 3, 5, 7, 30```
Your task is to find mobius(`n`)

# Input/Output


 - `[input]` integer `n`


 `2 <= n <= 1e12`


 - `[output]` an integer
"""

def mobius_function(n):
    """
    Calculate the Mobius function for a given integer n.

    Parameters:
    n (int): The input number for which the Mobius function is to be calculated.

    Returns:
    int: The value of the Mobius function for the given n.
    """
    prime_factors = set()
    p = 2
    while n > 1 and p <= n ** 0.5:
        while n % p == 0:
            if p in prime_factors:
                return 0
            prime_factors.add(p)
            n //= p
        p += 1 + (p != 2)
    return (-1) ** ((len(prime_factors) + (n != 1)) % 2)