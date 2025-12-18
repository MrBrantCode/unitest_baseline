"""
QUESTION:
*A Binod is a person who is very good with bitwise operations. Help Alice solve the following problem and become a Binod.*

You are given an array A of N elements. Process Q queries on this array, of the following form:
Each query contains 5 integers k, L_{1}, R_{1}, L_{2}, R_{2}. It is guaranteed that L_{1} ≤ R_{1} < L_{2} ≤ R_{2}.
The answer to a query is the number of pairs (i, j) such that:
- L_{1} ≤ i ≤ R_{1} and L_{2} ≤ j ≤ R_{2}
- A_{i} \oplus A_{j} has its k-th bit set. Here \oplus denotes the [bitwise XOR] operation.

Note: An integer x is said to have its k-th bit set if the (unique) binary representation of x contains 2^{k}. For example, 5 = 101_{2} = 2^{0} + 2^{2} has its zeroth and second bits set but not the first, while 16 = 10000_{2} = 2^{4} has only its fourth bit set.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of multiple lines of input.
- The first line of each test case contains two space-separated integers N and Q — the number of elements in array and number of queries, respectively.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}, \ldots, A_{N}.
- The next Q lines describe queries. The i-th of these Q lines contains 5 space-separated integers k, L_{1}, R_{1}, L_{2}, R_{2} — the parameters described in the statement.

------ Output Format ------ 

For each test case, output Q lines.The i-th of these lines should be the answer to the i-th query.

------ Constraints ------ 

$1 ≤ T ≤ 5 \cdot 10^{4}$
$2 ≤ N ≤ 10^{5}$
$1 ≤ Q ≤ 5\cdot 10^{5}$
$0 ≤ A_{i} < 2^{60}$
$1 ≤ L_{1} ≤ R_{1} < L_{2} ≤ R_{2} ≤ N$.
$0 ≤ k < 60$
- The sum of $N$ and $Q$ over all test cases won't exceed $10^{5}$ and $5\cdot 10^{5}$ respectively.

----- Sample Input 1 ------ 
2
5 2
1 2 4 3 2
1 1 3 5 5
2 1 2 3 5
6 2
3 5 6 13 12 20
1 1 4 5 6
3 2 3 4 6

----- Sample Output 1 ------ 
2
2
4
4
----- explanation 1 ------ 
Test case $1$: The array is $A = [1, 2, 4, 3, 2]$.
- Query $1$: the ranges are $[1, 3]$ and $[5, 5]$, and $k = 1$. There are three pairs of $(i, j)$: $(1, 5), (2, 5), (3, 5)$.
- $A_{1} \oplus A_{5} = 1 \oplus 2 = 3 = 11_{2}$ has its first bit set
- $A_{2} \oplus A_{5} = 2 \oplus 2 = 0 = 0_{2}$ doesn't have its first bit set
- $A_{3} \oplus A_{5} = 4 \oplus 2 = 6 = 110_{2}$ has its first bit set
- So, the answer is $2$.
- Query $2$: the ranges are $[1, 2]$ and $[3, 5]$, and now $k = 2$. This time, there are $6$ pairs of indices. Of them, it can be verified that $(1, 3)$ and $(2, 3)$ are the ones that satisfy the given condition.
"""

def count_pairs_with_kth_bit_set(arr, queries):
    n = len(arr)
    matrix = [[0 for _ in range(60)] for _ in range(n)]
    
    # Precompute the matrix
    for i in range(n):
        for j in range(60):
            if arr[i] & 1:
                matrix[i][j] += 1
                if i != 0:
                    matrix[i][j] += matrix[i - 1][j]
            else:
                matrix[i][j] += matrix[i - 1][j]
            arr[i] >>= 1
    
    results = []
    
    # Process each query
    for query in queries:
        k, l1, r1, l2, r2 = query
        l1 -= 1
        r1 -= 1
        l2 -= 1
        r2 -= 1
        
        ans1 = matrix[r1][k] if l1 == 0 else matrix[r1][k] - matrix[l1 - 1][k]
        ans2 = r1 - l1 + 1 - ans1
        ans3 = matrix[r2][k] - matrix[l2 - 1][k]
        ans4 = r2 - l2 + 1 - ans3
        
        results.append(ans1 * ans4 + ans2 * ans3)
    
    return results