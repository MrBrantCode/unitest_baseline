"""
QUESTION:
You are given $n$ positive integers $a_1, \ldots, a_n$, and an integer $k \geq 2$. Count the number of pairs $i, j$ such that $1 \leq i < j \leq n$, and there exists an integer $x$ such that $a_i \cdot a_j = x^k$.


-----Input-----

The first line contains two integers $n$ and $k$ ($2 \leq n \leq 10^5$, $2 \leq k \leq 100$).

The second line contains $n$ integers $a_1, \ldots, a_n$ ($1 \leq a_i \leq 10^5$).


-----Output-----

Print a single integer — the number of suitable pairs.


-----Example-----
Input
6 3
1 3 9 8 24 1

Output
5



-----Note-----

In the sample case, the suitable pairs are: $a_1 \cdot a_4 = 8 = 2^3$; $a_1 \cdot a_6 = 1 = 1^3$; $a_2 \cdot a_3 = 27 = 3^3$; $a_3 \cdot a_5 = 216 = 6^3$; $a_4 \cdot a_6 = 8 = 2^3$.
"""

from collections import defaultdict

def count_suitable_pairs(a, k):
    # Helper function to generate prime numbers up to the square root of the maximum element in a
    def generate_primes(max_val):
        n = int(max_val ** 0.5)
        mark = [True] * (n + 1)
        prime = []
        for i in range(2, n + 1):
            if mark[i]:
                for j in range(i, n + 1, i):
                    mark[j] = False
                prime.append(i)
        return prime
    
    # Generate primes up to the square root of the maximum element in a
    max_val = max(a)
    primes = generate_primes(max_val)
    
    # Dictionary to count occurrences of each tuple
    d = defaultdict(int)
    ans = 0
    
    for i in a:
        t, t1 = (), ()
        for prime in primes:
            if i == 1:
                break
            if i % prime == 0:
                count = 0
                while i % prime == 0:
                    i //= prime
                    count += 1
                z = count % k
                if z:
                    t += (prime, z)
                    t1 += (prime, k - z)
        if i > 1:
            t += (i, 1)
            t1 += (i, k - 1)
        ans += d[t1]
        d[t] += 1
    
    return ans