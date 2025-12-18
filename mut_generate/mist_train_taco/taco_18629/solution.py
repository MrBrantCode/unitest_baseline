"""
QUESTION:
For an array A of length N, let F(A) denote the sum of the product of all the subarrays of A. Formally,

F(A) = \sum_{L=1}^N \sum_{R=L}^N  (\prod_{i=L}^R A_{i}\right )

For example, let A = [1, 0, 1], then there are 6 possible subarrays:

Subarray [1, 1] has product = 1
Subarray [1, 2] has product = 0
Subarray [1, 3] has product = 0
Subarray [2, 2] has product = 0
Subarray [2, 3] has product = 0
Subarray [3, 3] has product = 1

So F(A) = 1+1 = 2.
  
Given a binary array A, determine the sum of F(A) over all the N! orderings of A modulo 998244353.

Note that orderings here are defined in terms of indices, not elements; which is why every array of length N has N! orderings. For example, the 3! = 6 orderings of A = [1, 0, 1] are:
[1, 0, 1] corresponding to indices [1, 2, 3]
[1, 1, 0] corresponding to indices [1, 3, 2]
[0, 1, 1] corresponding to indices [2, 1, 3]
[0, 1, 1] corresponding to indices [2, 3, 1]
[1, 1, 0] corresponding to indices [3, 1, 2]
[1, 0, 1] corresponding to indices [3, 2, 1]

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of multiple lines of input.
- The first line of each test case contains a single integer N denoting the le
- The second line contains N space-separated integers denoting the array A.

------ Output Format ------ 

For each test case, output the sum of F(A) over all the N! orderings of A, modulo 998244353.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ N ≤ 10^{5}$
$0 ≤ A_{i} ≤ 1$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
4
3
1 0 1
1
0
2
1 1
4
1 1 0 1

----- Sample Output 1 ------ 
16
0
6
120
"""

MOD = 998244353

# Precompute factorials and modular inverses
cpraid1 = [1] * 100001
cpraid2 = [1] * 100001
cpraid3 = [1] * 100001

for i in range(2, 100001):
    cpraid1[i] = cpraid1[i - 1] * i % MOD
    cpraid2[i] = MOD - MOD // i * cpraid2[MOD % i] % MOD
    cpraid3[i] = cpraid3[i - 1] * cpraid2[i] % MOD

def C(x, y):
    return 0 if x < 0 or y > x else cpraid1[x] * cpraid3[y] * cpraid3[x - y] % MOD

def calculate_sum_of_F_over_orderings(T, test_cases):
    results = []
    for (N, A) in test_cases:
        K = 0
        c = A.count(0)
        for i in range(N - c + 1):
            K += i * C(N - i, c) % MOD
        ans = K * (c + 1) * cpraid1[N - c] * cpraid1[c] % MOD
        results.append(ans)
    return results