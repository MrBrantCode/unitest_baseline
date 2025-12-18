"""
QUESTION:
Check if given numbers are prime numbers. 
If number N is prime ```return "Probable Prime"``` else ``` return "Composite"```. 
HINT: Upper bount is really big so you should use an efficient algorithm.

Input
  1 < N ≤ 10^(100)

Example
  prime_or_composite(2)  # should return Probable Prime
  prime_or_composite(200)  # should return Composite
"""

def is_probable_prime(n):
    if n < 4:
        return 'Probable Prime'
    if n % 2 == 0:
        return 'Composite'
    
    # Decompose (n-1) into the form d * 2^r
    (d, r) = (n - 1, 0)
    while d % 2 == 0:
        (d, r) = (d // 2, r + 1)
    
    # Perform Miller-Rabin primality test with base 2 and 31
    for a in [2, 31]:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return 'Composite'
            if x == n - 1:
                break
        else:
            return 'Composite'
    
    return 'Probable Prime'