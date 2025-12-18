"""
QUESTION:
Given an array A having N elements, a subarray S of A is called good if XOR(S) ≥ K, where XOR(S) denotes the [bitwise XOR] of all the elements of the subarray S.

Find the length of the smallest subarray S which is good. If there is no good subarray, print -1 instead. 

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of the T test cases follows.
- The first line of each test case contains two space-separated integers N and K - as described in the problem statement. 
- The second line of each test case contains N space-separated integers A_{1}, A_{2},..., A_{N}, A_{i} representing the elements of the array A.

------ Output Format ------ 

For each test case, output in a single line, the length of the shortest subarray which is good. If there is no good subarray, print -1.

------ Constraints ------ 

$1 ≤ T ≤ 2 \cdot 10^{4}$
$1 ≤ N ≤ 10^{5}$
$0 ≤ A_{i} < 2^{30}$
$0 ≤ K < 2^{31}$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
3
5 15
1 4 2 8 1
5 7
1 4 2 8 1
5 20
1 4 2 8 1
----- Sample Output 1 ------ 
4
1
-1
----- explanation 1 ------ 
Test case $1$:
For $S = [A_{1}, A_{2}, A_{3}, A_{4}]$, $XOR(S) = 1\oplus 4\oplus 2\oplus 8 = 15$. 
Similarly, for $S = [A_{2}, A_{3}, A_{4}, A_{5}]$, $XOR(S) = 4\oplus 2\oplus 8\oplus 1 = 15$. 
These are the only two subarrays which are good. The length of these subarrays is $4$. It can be proven that no subarray of length less than $4$ is good.

Test case $2$: There are several good subarrays. Some examples are $S = [A_{4}]$, $S = [A_{1}, A_{2}, A_{3}]$, 
and $S = [A_{3}, A_{4}]$. The length of the smallest subarray is $1$, and that subarray is $[A_{4}]$. It can be proven that no subarray of length less than $1$ is good.

Test case $3$: There is no subarray $S$ such that $XOR(S) ≥ 20$. Hence, there is no good subarray.
"""

def find_smallest_good_subarray_length(A, K):
    def length(getMask, ignoreMask):
        assert getMask & ignoreMask == 0
        C = [0]
        D = {0: 0}
        res = float('inf')
        for (i, elt) in enumerate(A):
            presum = C[-1] ^ elt & ~ignoreMask
            C.append(presum)
            comp = presum ^ getMask
            if comp in D:
                l = i + 1 - D[comp]
                res = min(res, l)
            D[C[-1]] = i + 1
        return res
    
    res = length(K, 0)
    ignoreMask = -1 & (1 << 32) - 1
    getMask = 0
    for k in range(31, -1, -1):
        ignoreMask ^= 1 << k
        if K & 1 << k != 0:
            getMask |= 1 << k
        else:
            getMask |= 1 << k
            res = min(res, length(getMask, ignoreMask))
            getMask ^= 1 << k
    
    return -1 if res == float('inf') else res