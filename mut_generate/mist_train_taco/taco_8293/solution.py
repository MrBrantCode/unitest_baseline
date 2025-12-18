"""
QUESTION:
Let's assume that 

  * v(n) is the largest prime number, that does not exceed n;
  * u(n) is the smallest prime number strictly greater than n. 



Find <image>.

Input

The first line contains integer t (1 ≤ t ≤ 500) — the number of testscases. 

Each of the following t lines of the input contains integer n (2 ≤ n ≤ 109).

Output

Print t lines: the i-th of them must contain the answer to the i-th test as an irreducible fraction "p/q", where p, q are integers, q > 0.

Examples

Input

2
2
3


Output

1/6
7/30
"""

def find_prime_fractions(t, test_cases):
    MAX = 33000
    bePrime = [0] * MAX
    primNum = []
    
    # Sieve of Eratosthenes to find all primes up to MAX
    for j in range(2, MAX):
        if bePrime[j] == 0:
            primNum.append(j)
            i = j
            while i < MAX:
                bePrime[i] = 1
                i = i + j

    def isPrime(a):
        for j in primNum:
            if j >= a:
                return True
            if a % j == 0:
                return False
        return True

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    results = []
    
    for n in test_cases:
        m = n
        while not isPrime(m):
            m -= 1
        while not isPrime(n + 1):
            n += 1
        
        a = n - 1
        b = 2 * (n + 1)
        num = n - m
        a = a * (n + 1) * m - num * b
        b = b * (n + 1) * m
        g = gcd(a, b)
        a //= g
        b //= g
        results.append(f'{a}/{b}')
    
    return results