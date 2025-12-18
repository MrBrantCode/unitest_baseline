"""
QUESTION:
You are given a polynomial of degree N with integer coefficients: f(x)=a_Nx^N+a_{N-1}x^{N-1}+...+a_0. Find all prime numbers p that divide f(x) for every integer x.

Constraints

* 0 \leq N \leq 10^4
* |a_i| \leq 10^9(0\leq i\leq N)
* a_N \neq 0
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
a_N
:
a_0


Output

Print all prime numbers p that divide f(x) for every integer x, in ascending order.

Examples

Input

2
7
-7
14


Output

2
7


Input

3
1
4
1
5


Output




Input

0
998244353


Output

998244353
"""

def find_prime_divisors_of_polynomial(N, A):
    def factors(z):
        ret = []
        for i in range(2, int(z ** (1 / 2)) + 1):
            if z % i == 0:
                ret.append(i)
                while z % i == 0:
                    z //= i
        if z != 1:
            ret.append(z)
        return ret

    def eratosthenes(N):
        if N == 0:
            return []
        work = [True] * (N + 1)
        work[0] = False
        work[1] = False
        ret = []
        for i in range(N + 1):
            if work[i]:
                ret.append(i)
                for j in range(2 * i, N + 1, i):
                    work[j] = False
        return ret

    Primes = eratosthenes(N)
    ANS = []
    F = factors(abs(A[0]))
    
    for f in F:
        if f >= N + 1:
            Primes.append(f)
    
    for p in Primes:
        if p >= N + 1:
            check = 1
            for i in range(N + 1):
                if A[i] % p != 0:
                    check = 0
                    break
            if check == 1:
                ANS.append(p)
        else:
            poly = [0] * (p - 1)
            for i in range(N + 1):
                poly[(N - i) % (p - 1)] = (poly[(N - i) % (p - 1)] + A[i]) % p
            check = 0
            if sum(poly) == 0 and A[N] % p == 0:
                check = 1
            if check == 1:
                ANS.append(p)
    
    return ANS