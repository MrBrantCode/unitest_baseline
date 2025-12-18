"""
QUESTION:
How many non decreasing sequences are there of length ${K}$, with the condition that numbers in sequence can take values only from $1,2,3,\cdots N$ and gcd of all numbers in the sequence must be ${1}$.

Input Format 

The first line contains an integer ${T}$ i.e. the number of test cases.

${T}$ lines follow, each line containing two integers $N$ and ${K}$ separated by a single space.  

Output Format 

For each testcase, print in a newline the answer $\:\text{mod}\:(10^9+7)$. 

Constraints  

$1\leq T\leq5$ 

$1\leq N\leq10^5$ 

$1\leq K\leq10^5$  

Sample Input

4
2 4 
3 4
5 2
1 10

Sample Output

4
13
10
1

Explanation

For the first testcase, the sequences are 

(1,1,1,1), (1,1,1,2), (1,1,2,2), (1,2,2,2) = 4

For the second testcase, the sequences are 

(1,1,1,1), (1,1,1,2), (1,1,1,3), (1,1,2,2), (1,1,2,3), (1,1,3,3)
(1,3,3,3), (1,2,2,2), (1,2,2,3), (1,2,3,3), (2,2,2,3), (2,2,3,3), (2,3,3,3)

which are 13 in number.  

For the third testcase, the sequences are  

(1,1), (1,2), (1,3), (1,4), (1,5), (2,3), (2,5), (3, 4), (3, 5), (4, 5) = 10

for the fourth testcase, the only sequence is 

(1,1,1,1,1,1,1,1,1,1)
"""

def count_non_decreasing_sequences(N, K, MOD=10**9 + 7):
    def primeSieve(n):
        A = [0, 0] + [1 for i in range(n - 1)]
        sqrtN = int(n ** 0.5)
        for i in range(2, sqrtN + 1):
            if A[i] == 1:
                for j in range(i * i, n + 1, i):
                    A[j] = 0
        return [i for (i, prime) in enumerate(A) if prime]

    def moebiusSieve(N):
        P = primeSieve(N + 1)
        Mu = [1] * (N + 1)
        Mu[0] = 0
        for p in P:
            for q in range(p, N + 1, p):
                Mu[q] *= -1
            for q in range(p * p, N + 1, p * p):
                Mu[q] = 0
        return Mu

    def factAndInvFactTables(n, m):
        (fact, invFact) = ([1] + n * [0], [1] + n * [0])
        for k in range(1, n + 1):
            fact[k] = fact[k - 1] * k % m
        invFact[n] = pow(fact[n], m - 2, m)
        for k in range(n, 1, -1):
            invFact[k - 1] = invFact[k] * k % m
        return (fact, invFact)

    mu = moebiusSieve(10 ** 5)
    s = 0
    (fact, invFact) = factAndInvFactTables(N + K, MOD)
    for i in range(1, N + 1):
        s = (s + mu[i] * (fact[N // i + K - 1] * invFact[K] * invFact[N // i - 1]) % MOD) % MOD
    return s