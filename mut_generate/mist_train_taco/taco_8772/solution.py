"""
QUESTION:
Read problem statements in [Russian], [Mandarin Chinese], [Bengali], and [Vietnamese] as well.

You are given an array A consisting of N integers and Q queries. Each query is described by two integers L and R. For each query, output the number of tuples (i, j, k) such that L≤ i< j< k≤ R and A_{i}+A_{j}+A_{k} is an even number.

------ Input Format ------ 

- The first line contains an integer T, the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers N and Q.
- The next line contains N integers A_{1},\ldots,A_{N}.
- Then Q lines follow, each containing two integers L_{i} and R_{i}.

------ Output Format ------ 

For each query, output the number of tuples possible as mentioned in the problem statement.

------ Constraints ------ 

$1 ≤ T ≤ 10^{3}$
$1 ≤ N, Q ≤ 10^{5}$
$0 ≤ A_{i} ≤ 10^{6}$
$1 ≤ L_{i} ≤ R_{i} ≤ N$
- The sum of $N$ over all test cases does not exceed $10^{6}$.
- The sum of $Q$ over all test cases does not exceed $10^{5}$

----- Sample Input 1 ------ 
1
6 3
1 2 3 4 5 6
1 3
2 5
1 6
----- Sample Output 1 ------ 
1
2
10
----- explanation 1 ------ 
- For the first query, we can choose $(1, 2, 3)$ since $A_{1} + A_{2} + A_{3} = 6$ is an even 
number.
- For the second query, we can choose $(2, 3, 5)$ since $A_{2} + A_{3} + A_{5} = 10$ is even, and $(3, 4, 5)$ since $A_{3} + A_{4} + A_{5} = 12$ is even.
"""

def count_even_sum_tuples(N, Q, A, queries):
    even = [0] * N
    odd = [0] * N
    
    for i in range(N):
        even[i] += even[max(i - 1, 0)]
        odd[i] += odd[max(i - 1, 0)]
        if i != N - 1:
            if A[i] % 2:
                odd[i + 1] += 1
            else:
                even[i + 1] += 1
    
    results = []
    for L, R in queries:
        L -= 1
        R -= 1
        num_evens = even[R] - even[L] + 1 * (not A[R] % 2)
        num_odds = odd[R] - odd[L] + 1 * (A[R] % 2)
        choose2 = num_odds * (num_odds - 1) // 2 * num_evens
        choose3 = num_evens * (num_evens - 1) * (num_evens - 2) // 6
        results.append(choose2 + choose3)
    
    return results