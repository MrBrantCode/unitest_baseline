"""
QUESTION:
Read problem statements in [Mandarin], [Bengali], [Russian], and [Vietnamese] as well.

You are given a sequence A_{1}, A_{2}, \ldots, A_{N} which contains pairwise distinct elements and a sequence B_{1}, B_{2}, \ldots, B_{N}, which also contains pairwise distinct elements (but not necessarily distinct from elements of A). For each valid i, 1 ≤ A_{i}, B_{i} ≤ 2 \cdot N.

You may rotate B as many times as you want. A rotation consists of moving the first element of the sequence to the end. Afterwards, let's define a sequence C_{1}, C_{2}, \ldots, C_{N} as C_{i} = (A_{i} + B_{i}) \% N for each valid i.

There are N possible sequences C. Find the lexicographically smallest of these sequences.

Note: A sequence x is lexicographically smaller than a different sequence y if x_{i} < y_{i}, where i is the smallest valid index where the sequences x and y differ.

------ Input Format ------ 

- The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains a single integer N.
- The second line contains N space-separated integers A_{1}, A_{2}, \ldots, A_{N}. 
- The third line contains N space-separated integers B_{1}, B_{2}, \ldots, B_{N}. 

------ Output Format ------ 

For each test case, print a single line containing N space-separated integers C_{1}, C_{2}, \ldots, C_{N} denoting the lexicographically smallest sequence.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ N ≤ 10^{5}$
$1 ≤ A_{i}, B_{i} ≤ 2 \cdot N$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$

------ subtasks ------ 

Subtask #1 (100 points): original constraints

----- Sample Input 1 ------ 
1
3
1 4 5
1 3 4
----- Sample Output 1 ------ 
1 2 0
----- explanation 1 ------ 
Example case 1: After rotating $B$ once, it becomes $(3,4,1)$. Now $C = (1,2,0)$. This is the lexicographically smallest of all possible sequences $C$.
"""

def find_lexicographically_smallest_sequence(N, A, B):
    # Initialize variables
    a1 = 0
    m = (A[0] + B[0]) % N
    
    # Find the first rotation index a1
    for i in range(1, N):
        b = (A[0] + B[i]) % N
        if m > b:
            m = b
            a1 = i
    
    # Find the second rotation index a2 if exists
    a2 = -1
    for i in range(N):
        if (A[0] + B[i]) % N == m and i != a1:
            a2 = i
            break
    
    # Double the B array to facilitate rotation
    B *= 2
    
    # Generate sequence C for rotation a1
    C = [(A[i] + B[i + a1]) % N for i in range(N)]
    
    # If a2 exists, generate sequence D for rotation a2 and compare
    if a2 != -1:
        D = [(A[i] + B[i + a2]) % N for i in range(N)]
        if D < C:
            return D
    
    return C