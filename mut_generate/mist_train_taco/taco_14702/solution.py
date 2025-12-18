"""
QUESTION:
General primality test are often computationally expensive, so in the biggest prime number race the idea is to study special sub-families of prime number and develop more effective tests for them. 

[Mersenne Primes](https://en.wikipedia.org/wiki/Mersenne_prime) are prime numbers of the form: Mn = 2^(n) - 1. So far, 49 of them was found between M2 (3) and M74,207,281 which contains 22,338,618 digits and is (by September 2015) the biggest known prime. It has been found by GIMPS (Great Internet Mersenne Prime Search), wich use the test srudied here. (plus heuristics mentionned below)

Lucas and Lehmer have developed a [simple test](https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test) for Mersenne primes: 

> for `p` (an odd prime), the Mersenne number Mp is prime if and only if `S(p − 1) = 0 mod Mp`,

>where `S(n + 1) = S(n) * S(n) − 2` and `S(1) = 4`

The goal of this kata is to implement this test. Given an integer `>=2`, the program should calculate the sequence `S(n)` up to `p-1` and calculate the remainder modulo `Mp`, then return `True` or `False` as a result of the test. The case `n = 2` should return `True`.

You should take advantage of the fact that:

```k = (k mod 2^n + floor(k/2^n)) mod Mn```

Or in other words, if we take the least significant `n` bits of `k`, and add the remaining bits of `k`, and then do this repeatedly until at most `n` bits remain, we can compute the remainder after dividing `k` by the Mersenne number `2^n−1` without using division.

This test can be improved using the fact that if `n` is not prime, `2^n-1` will not be prime. So in theory you can test for the primality of `n` beforehand. But in practice the test for the primality of `n` will rapidly outgrow in difficulty the Lucas-Lehmer test. So we can only use heuristics to rule out `n` with small factors but not complete factorization algorithm. You don't need to implement such heuristics here. 

The rapid growth of `s^2` makes javascript reach its integer limit quickly (coherent result for `n = 13`, but not `17`). Whereas python seems to be only limited by the execution time limit and let us see that M11,213 is prime (contains 3376 digits).
"""

def is_mersenne_prime(n):
    """
    Determines if a Mersenne number Mn = 2^n - 1 is a prime using the Lucas-Lehmer test.

    Parameters:
    n (int): The exponent in the Mersenne prime formula, where n >= 2.

    Returns:
    bool: True if Mn is a Mersenne prime, otherwise False.
    """
    if n == 2:
        return True
    
    # Calculate the Mersenne number Mp = 2^n - 1
    Mp = (1 << n) - 1
    
    # Initialize the Lucas-Lehmer sequence
    S = 4
    
    # Perform the Lucas-Lehmer test
    for _ in range(n - 2):
        S = (S * S - 2) % Mp
    
    # Mp is prime if and only if S(n-1) % Mp == 0
    return S == 0