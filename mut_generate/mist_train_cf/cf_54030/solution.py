"""
QUESTION:
Write a function `P(n)` that computes the number of primitive Pythagorean triplets where `a` is less than `b`, which is less than `c`, and `c` is less than or equal to `n`. A primitive Pythagorean triplet is defined as a set of three positive integers `a`, `b`, and `c` that satisfy the equation `a^2+b^2=c^2` and are coprime. 

Note that the input `n` can be very large and the function should be optimized for performance.
"""

def gcd(m, n):    
    """Computes the greatest common divisor of m and n."""
    while n!=0:
        m, n = n, m % n
    return m

def P(n):
    """Computes the number of primitive Pythagorean triplets with c less than or equal to n."""
    res = 0
    m = 2
    while (m*m) <= n:
        for mn in range(1 if m%2==0 else 2, m, 2):
            if gcd(m, mn)==1:
                if m*(m+mn) <= n:
                    res += min(m, (n//mn - m)>>1)
        m += 1
    return res