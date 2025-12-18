"""
QUESTION:
A number is algebraic if it is a root of some nonzero polynomial with integer coefficients. A number is transcendental if it is not algebraic.

For example, ${11}$, ${i}$, $\sqrt[3]{2}$ and $\phi$ (golden ratio) are algebraic, because they are roots of $x-11$, $x^2+1$, $x^3-2$ and $x^2-x-1$, respectively. Also, it can be shown that the sum and product of two algebraic numbers is also algebraic, so for example $24+i$, $\sqrt{2}+\sqrt{3}$ and $\sqrt[3]{{11}}\phi$ are also algebraic. However, it has been shown by Lindemann that ${\pi}$ is transcendental.

The degree of an algebraic number is the minimal degree of a polynomial with integer coefficients in which it is a root. For example, the degrees of $5$, ${i}$, $\sqrt[3]{2}$ and $\phi$ are ${1}$, $2$, $3$ and $2$, respectively.

Given $N$ positive integers ${A_1}$, ${A_{2}}$, ..., ${A}_N$, calculate the degree of the following algebraic number:
$\sqrt{A_1}+\sqrt{A_2}+\sqrt{A_3}+\text{}\cdots+\sqrt{A_N}$  

Input Format 

The first line of input contains ${T}$, the number of test cases. The descriptions of the test cases follow.

Each test case has two lines of input. The first line contains a single integer, $N$. The second line contains $N$ integers ${A_1}$, ..., $A_N$ separated by single spaces.

Output Format 

For each test case, output one line containing exactly one integer, which is the answer for that test case.

Constraints 

$1\leq T\leq10^5$ 

$1\leq N\leq50$ 

$1\leq A_i\leq10^7$ 

The sum of the $N$'s in a single test file is at most $10^{5}$  

Sample Input  

3
1
4
3
2 4 4
4
1 2 3 5

Sample Output 

1
2
8

Explanation 

Case 1: A minimal polynomial of $\sqrt{4}$ is $2x-4$.  

Case 2: A minimal polynomial of $\sqrt{2}+\sqrt{4}+\sqrt{4}$ is $x^2-8x+14$.  

Case 3: A minimal polynomial of $\sqrt1+\sqrt{2}+\sqrt{3}+\sqrt{5}$ is:
$x^8-8x^7-12x^6+184x^5-178x^4-664x^3+580x^2+744x-71$
"""

def calculate_algebraic_degree(test_cases):
    MAXA = 10 ** 7
    
    def allprimes(upto):
        primes = []
        seive = [True] * (upto + 1)
        for i in range(2, upto + 1):
            if seive[i]:
                primes.append(i)
                for j in range(i * i, upto + 1, i):
                    seive[j] = False
        return primes
    
    def factoroddpow(n, primelist=allprimes(int(MAXA ** 0.5))):
        ans = []
        for prime in primelist:
            if n % prime == 0:
                deg = 0
                while n % prime == 0:
                    n //= prime
                    deg += 1
                if deg & 1 == 1:
                    ans.append(prime)
        if n > 1:
            ans.append(n)
        return ans
    
    def mindegree(a):
        factors = [set(factoroddpow(item)) for item in a]
        adjoins = 0
        for (i, factor) in enumerate(factors):
            if len(factor) == 0:
                continue
            sample = next(iter(factor), None)
            for otherfactor in factors[i + 1:]:
                if sample in otherfactor:
                    otherfactor ^= factor
            adjoins += 1
        return 1 << adjoins
    
    results = []
    for case in test_cases:
        N, A = case
        results.append(mindegree(A))
    
    return results