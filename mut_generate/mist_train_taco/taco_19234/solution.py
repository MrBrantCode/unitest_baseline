"""
QUESTION:
Given an array of N integers and another array R containing Q queries(of l and r). Answer all Q queries asking the number of primes in the subarray ranging from l to r (both inclusive).
Note: A is 0-based but the queries will be 1-based.
Example 1:
Input:
N=5,Q=3
A={2,5,6,7,8}
R={{1,3},{2,5},{3,3}}
Output:
2 2 0
Explanation:
There are 2 primes in the range [1,3], 
which are 2 and 5.
There are 2 primes in the range [2,5],
which are 5 and 7.
There are no primes in the range [3,3].
Example 2:
Input:
N=5,Q=3
A={1,2,3,4,5}
R={{1,4},{2,5},{2,3}}
Output:
2 3 2
Explanation:
There are 2 primes in range [1,4],
which are 2 and 3.
There are 3 primes in the range [2,5],
which are 2,3 and 5.
There are 2 primes in the range [3,3],
which are 2 and 3.
Your Task:
You don't need to read input or print anything. Your task is to complete the function primeRange() which takes the two numbers N and Q as well as the two arrays A and Q as input parameters and returns the answers of all Q queries.
Expected Time Complexity:O(Max(A[i])*Log(Log (Max(A[i]) )))
Expected Auxillary Space:O(Max(A[i]))
Note:  Max(A[i]) represents the maximum value in the array A
Constraints:
1<=N,Q,A[i]<=10^{6}
1<=l<=r<=N
"""

def prime_range(N, Q, A, R):
    n = max(A)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    # Sieve of Eratosthenes to find all primes up to n
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    
    tree = [0] * (n + 1)

    def add(pos, val):
        while pos <= n:
            tree[pos] += val
            pos += pos & -pos

    def helper(pos):
        res = 0
        while pos > 0:
            res += tree[pos]
            pos -= pos & -pos
        return res

    def get(a, b):
        if a == 1:
            return helper(b)
        return helper(b) - helper(a - 1)
    
    # Populate the Fenwick Tree with prime counts
    for (i, x) in enumerate(A):
        if sieve[x]:
            add(i + 1, 1)
    
    # Answer the queries
    return [get(l, r) for (l, r) in R]