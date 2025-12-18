"""
QUESTION:
A Nice-P sequence is defined as a sequence such that a1 x a2=1 (mod p), a2 x a3=1 (mod p) ..., an-1 x an = 1 (mod p). In addition, a1, a 2, a 3, ... an must be less than p and greater than or equal to 0. Given one element, a1, find the sum of the entire Nice-P sequence of length n. If, for any ai, where i ≥ 1, there exists no ai+1 such that ai x ai+1 = 1 (mod p), output -1. 

NOTE: p IS NOT NECESSARILY A PRIME

Input:

The first line contains T, the number of test cases.

T lines follow, each containing a1, p, and n.

Output:

For each test case, output one line, the required sum. 

Constraints:

1 ≤ T ≤ 10^5 
1 ≤ a1 ≤ 10^5
1 ≤ n ≤ 10^9
a1 < p ≤10^9

SAMPLE INPUT
2
2 3 2
3 7 2

SAMPLE OUTPUT
4
8

Explanation

In the first test case, the P-interesting sequence will be 2, 2, which has a sum of 4. In the second test case, it will be 3, 5, which has a sum of 8.
"""

def calculate_nice_p_sequence_sum(a1, p, n):
    """
    Calculate the sum of the Nice-P sequence of length n starting with a1 modulo p.
    
    Parameters:
    a1 (int): The first element of the sequence.
    p (int): The modulus.
    n (int): The length of the sequence.
    
    Returns:
    int: The sum of the Nice-P sequence or -1 if no valid sequence exists.
    """
    
    def gcd(a, b):
        while b: a, b = b, a % b
        return a

    def extgcd(a, b):
        u0, u1 = 1, 0
        if b == 0:
            return u0, u1

        d0, d1 = a, b
        while 1:
            q, r = d0 // d1, d0 % d1
            if r == 0:
                return u1, (d1 - a * u1) // b

            d0, d1 = d1, r
            u0, u1 = u1, u0 - q * u1

    def mod_inverse(a, p):
        x, y = extgcd(a, p)
        return (p + x % p) % p

    if gcd(a1, p) != 1:
        return -1

    b = mod_inverse(a1, p)
    ans = (a1 + b) * (n // 2) + (a1 if n % 2 else 0)
    return ans