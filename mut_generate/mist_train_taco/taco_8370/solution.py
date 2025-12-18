"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

You are given two positive integers $N, K$, where $K ≤ N$. Your goal is to find the number of permutations of $\{1, 2, ..., N\}$ with exactly $K$ [inversions]. As the answer may be very large, you only need to find it modulo $2$.

------ Input: ------

The first line contains one integer $T$, the number of test cases. Then the test cases follow. 
Each test case contains a single line of input, two integers $N, K$. 

------ Output: ------
For each test case, print one integer: the number of permutation of $N$ elements with $K$ inversions, modulo $2$.

------ Constraints  ------
$1 ≤ T ≤ 100$
$0 ≤ K ≤ N ≤ 2 \cdot 10^{10}$

------ Subtasks ------
10 points : $1 ≤ N ≤ 200$
10 points : $1 ≤ N ≤ 2000$
10 points : $1 ≤ N ≤ 200\,000$
10 points : $1 ≤ N ≤ 2\,000\,000$
60 points : $1 ≤ N ≤ 2 \cdot 10^{10}$

----- Sample Input 1 ------ 
11  

10 0  

10 1  

10 2   

10 3  

10 4  

10 5  

10 6  

10 7  

10 8  

10 9   

10 10
----- Sample Output 1 ------ 
1  

1  

0  

1  

0  

0  

0  

1  

1  

0  

0
"""

def count_permutations_with_inversions(N, K):
    count = 0
    
    if N == 0:
        return 0
    
    if K == 0:
        return 1
    
    z = (N - 1) & K
    if z == 0:
        count += 1
    
    x = ((1 + 24 * K) ** 0.5 - 1) / 6
    y = x
    x = int(x)
    
    for j in range(1, x + 1):
        u = j * (3 * j - 1) // 2
        a = N + K - j - 1 - u
        b = K - j - u
        z = (a - b) & b
        if z == 0:
            count += 1
        a += j
        b += j
        z = (a - b) & b
        if z == 0:
            count += 1
    
    x2 = y + 1 / 3
    x2 = int(x2)
    
    for j in range(x + 1, x2 + 1):
        u = j * (3 * j - 1) // 2
        a = N + K - 1 - u
        b = K - u
        z = (a - b) & b
        if z == 0:
            count += 1
    
    return count % 2