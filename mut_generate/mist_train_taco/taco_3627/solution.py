"""
QUESTION:
*After getting lost in Hollywood, ibti decided to give you yet another problem related to permutations.*

Consider a permutation P of length 2\cdot N.  
An array A of size N is generated using the permutation P, such that the i^{th} element of the array is a pair having value, A_{i} = (P_{i} \bmod N, P_{(i+N)} \bmod N).

The permutation P (of length 2\cdot N) is called N-beautiful, if, all elements of the array A are distinct.

Given integers K and M, your task is to count the number of i-beautiful permutations for each 1 ≤ i ≤ K. 

Since the answers can be large, print them modulo M.

------ Input Format ------ 

The first and only line of the input contains two space-separated integers K, M - the parameters defined in the statement.

------ Output Format ------ 

Print K space-separated integers, the i^{th} integer will denote the number of i-beautiful permutations modulo M.

------ Constraints ------ 

$1 ≤K ≤2 \cdot 10^{5}$
$10^{7} + 19 ≤M ≤10^{9}+7$
- It is guaranteed that $M$ is a prime number.

------ subtasks ------ 

Subtask 1 (50 points): $1 ≤ K ≤ 10^{3}$
Subtask 2 (50 points): No further constraints.

----- Sample Input 1 ------ 
8 269696969
----- Sample Output 1 ------ 
2 16 576 34560 3110400 142258231 78756849 13872609
----- explanation 1 ------ 
- All permutations of length $2$ are $1$-beautiful, thus the first value we print is $2! = 2$.
- There are $16$ $2$-beautiful permutations out of the $24$ possible permutations. The $8$ non-beautiful permutations are: $\{1, 3, 2, 4\}, \{1, 3, 4, 2\}, \{2, 4, 1, 3\}, \{2, 4, 3, 1\}, \{3, 1, 2, 4\}, \{3, 1, 4, 2\}, \{4, 2, 1, 3\}, \{4, 2, 3, 1\}$  
For example, the permutation $\{1, 3, 2, 4\}$ is not beautiful as $A = [(1 \bmod 2, 2 \bmod 2), (3 \bmod 2, 4 \bmod 2)] = [(1, 0), (1, 0)]$. Both elements of the array $A$ are same.
"""

def count_i_beautiful_permutations(k, m):
    if k <= 2:
        return [2 % m, 16 % m][:k]
    
    b = [1, 2 % m, 16 % m]
    for n in range(2, k):
        b.append((n + 1) * ((2 + 4 * n) * b[n] - 4 * n ** 2 * b[n - 1] + 16 * n ** 2 * (n - 1) ** 2 * b[n - 2]) % m)
    
    return b[1:]