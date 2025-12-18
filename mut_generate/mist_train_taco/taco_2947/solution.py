"""
QUESTION:
You love array, don't you?

You are given two integer N and M, along with an array B of length N containing pairwise distinct integers. You have to find the number of array A of length N satisfying the follow conditions:

1. 1 ≤ A_{i} ≤ M.
2. A_{i} \neq A_{j} for all 1 ≤ i < j ≤ N.
3. A_{i} \neq B_{i} for all 1 ≤ i ≤ N.

Since the answer can be very large, output it under modulo 10^{9} + 7.

------ Input Format ------ 

- The first line of the input contains two space-separated integers N and M.
- The second line of the input contains N separated integers B_{1}, B_{2}, \dots, B_{N} - the array B.

------ Output Format ------ 

Output on a single line the number of satisfactory array modulo 10^{9} + 7.

------ Constraints ------ 

$1 ≤ N ≤ 2 \cdot 10^{5}$
$1 ≤ M ≤ 3 \cdot 10^{5}$
$1 ≤ B_{i} ≤ 10^{9}$
$B_{i} \neq B_{j}$ for all $1 ≤i < j ≤N$.

------ subtasks ------ 

Subtask $1$ (30 points): $1 ≤ R ≤ 10\,000$
Subtask $2$ (70 points): $1 ≤ R ≤ 10^{9}$

----- Sample Input 1 ------ 
3 4
5 1 2
----- Sample Output 1 ------ 
14
----- explanation 1 ------ 
All satisfactory arrays are:
- $[1, 2, 3]$
- $[2, 3, 1]$
- $[3, 2, 1]$
- $[1, 2, 4]$
- $[2, 4, 1]$
- $[4, 2, 1]$
- $[1, 3, 4]$
- $[1, 4, 3]$
- $[3, 4, 1]$
- $[4, 3, 1]$
- $[2, 3, 4]$
- $[2, 4, 3]$
- $[3, 2, 4]$
- $[4, 2, 3]$

----- Sample Input 2 ------ 
2 2
1 3
----- Sample Output 2 ------ 
1
----- explanation 2 ------ 
The only satisfactory array is:
- $[2, 1]$
"""

def count_satisfactory_arrays(N, M, B):
    mod = 10**9 + 7

    def ModInverse(n):
        return pow(n, mod - 2, mod)

    def NChooseK(n, k):
        return Factorial[n] * ModInverse(Factorial[n - k] * Factorial[k]) % mod

    if M < N:
        return 0

    Factorial = [1]
    for n in range(1, M + 1):
        Factorial.append(Factorial[-1] * n % mod)

    num_elements_in_bounds = sum(1 for x in B if x <= M)
    ans = NChooseK(M, N) * Factorial[N] % mod
    sign = -1

    for min_num_overlaps in range(1, num_elements_in_bounds + 1):
        delta = (NChooseK(num_elements_in_bounds, min_num_overlaps) * 
                 NChooseK(M - min_num_overlaps, N - min_num_overlaps) * 
                 Factorial[N - min_num_overlaps])
        delta %= mod
        ans = (ans + sign * delta) % mod
        sign *= -1

    return ans