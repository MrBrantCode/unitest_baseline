"""
QUESTION:
The function $g(n)$ represents the count of methods a positive integer $n$ can be expressed in the equation $x^2+xy+41y^2$, where $x$ and $y$ are integers. Given the function $\displaystyle T(N)=\sum_{n=1}^{N}g(n)$ and the values $T(10^3)=474$ and $T(10^6)=492128$, write a function to calculate the approximate value of $T(10^{16})$.
"""

def T(N):
    """
    Calculate the approximate value of T(N) for given N.
    """
    d = 0.474
    return d * N**(3/2)

# To calculate T(10^16), use:
# T_10_16 = T(10**16)