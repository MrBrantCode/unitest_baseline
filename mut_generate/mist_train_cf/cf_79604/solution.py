"""
QUESTION:
Determine the value of the function S(n) = ∑ a + b + c over all unique sets of three distinct prime numbers (a, b, c) where a < b < c < n, and the sequence a+1, b+1, and c+1 constitutes a geometric progression. Specifically, find S(10^8). The solution should be efficient given the high computational complexity of the problem.
"""

def S(n):
    def primes(n):
        sieve = np.ones(n//3 + (n%6==2), dtype=bool)
        sieve[0] = False
        for i in range(int(n**0.5)//3+1):
            if sieve[i]:
                k=3*i+1|1
                sieve[       ((k*k)//3)      ::2*k] = False
                sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
        return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

    primes_list = primes(n)
    total_sum = 0

    for i in range(len(primes_list)):
        for j in range(i+1, len(primes_list)):
            a = primes_list[i]
            b = primes_list[j]
            c = b*b/a
            if c < n and c%1 == 0 and c in primes_list:
                total_sum += a + b + int(c)
    return total_sum