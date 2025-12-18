"""
QUESTION:
Read problems statements [Mandarin] , [Bengali] , [Hindi] , [Russian] and [Vietnamese] as well.

You are given an integer sequence $A$ with length $N$. Find the number of ordered pairs of positive integers $(a, b)$ such that $a$ occurs in $A$ at least $b$ times and $b$ occurs in $A$ at least $a$ times. 

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
The second line contains $N$ space-separated integers $A_{1}, A_{2}, \dots, A_{N}$.

------  Output ------
For each test case, print a single line containing one integer — the number of pairs.

------  Constraints  ------
$1 ≤ T ≤ 1,000$
$2 ≤ N ≤ 10^{6}$
$1 ≤ A_{i} ≤ 10^{6}$ for each valid $i$
the sum of $N$ over all test cases does not exceed $3 \cdot 10^{6}$

------  Subtasks ------
Subtask #1 (30 points):
$1 ≤ N ≤ 10^{5}$
the sum of $N$ over all test cases does not exceed $3 \cdot 10^{5}$

Subtask #2 (70 points): original constraints

----- Sample Input 1 ------ 
3

5

1 2 3 4 5

5

1 1 2 2 3

5

3 3 2 2 2
----- Sample Output 1 ------ 
1

4

3
"""

def count_valid_pairs(test_cases):
    results = []
    
    for case in test_cases:
        N, A = case
        d = {}
        for j in A:
            d[j] = d.get(j, 0) + 1
        
        A.sort()
        s = 0
        c = 0
        
        for k in range(len(A)):
            if k == 0:
                s = 1
            elif A[k] != A[k - 1]:
                s = 1
            else:
                s += 1
            
            if d.get(s, 0) >= A[k]:
                c += 1
        
        results.append(c)
    
    return results