"""
QUESTION:
Given two positive integers N and M, let S denote the set of all the arrays of size N such that each element of the array lies in the range [1, M]. Since there are M^{N} such arrays, the size of S is M^{N}.

Let X_{i} denote the [bitwise AND] of all elements of the i^{th} array in the set, where 1 ≤ i ≤ M^{N}.  
Find the value \sum_{i = 1}^{M^{N}} X_{i}. Since the answer can be huge, output the answer modulo 998244353.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- The first and only line of each test case contains two integers N and M, the size of the array, and the maximum limit of elements.

------ Output Format ------ 

For each test case, print the value \sum_{i = 1}^{M^{N}} X_{i}. Since the answer can be huge, output the answer modulo 998244353.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ N ≤ 2\cdot10^{5}$
$1 ≤ M ≤ 10^{9}$

----- Sample Input 1 ------ 
2
2 2
2 3

----- Sample Output 1 ------ 
3
12
----- explanation 1 ------ 
Test case $1$: The set $S$ contains $\{[1,1], [1,2], [2,1], [2,2]\}$. The array $X = [1\& 1, 1\& 2, 2\& 1, 2\& 2] = [1, 0, 0, 2]$. Thus, sum of all elements of $X$ is $1+0+0+2 = 3$.

Test case $2$: The set $S$ contains $\{[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]\}$. The array $X = [1\& 1, 1\& 2, 1\& 3, 2\& 1, 2\& 2, 2\& 3, 3\& 1, 3\& 2, 3\& 3] = [1, 0, 1, 0, 2, 2, 1, 2, 3]$. Thus, sum of all elements of $X$ is $12$.
"""

def calculate_bitwise_and_sums(test_cases):
    mod = 998244353

    def counts(m, i):
        count = m >> i + 1 << i
        if m >> i & 1:
            count += m & (1 << i) - 1
        return count

    def solve(n, m):
        ans = 0
        for i in range(32):
            count = counts(m + 1, i)
            if count:
                ans = (ans + pow(count, n, mod) * pow(2, i, mod) % mod) % mod
            else:
                break
        return ans

    results = []
    for n, m in test_cases:
        results.append(solve(n, m))
    
    return results