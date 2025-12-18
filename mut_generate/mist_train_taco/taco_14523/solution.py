"""
QUESTION:
Read problems statements [Bengali] , [Mandarin chinese] , [Russian] and [Vietnamese] as well.

There are two sequences $A_{1}, A_{2}, \dots, A_{N}$ and $B_{1}, B_{2}, \dots, B_{N}$. Answer $Q$ queries on these sequences.

In each query, you should calculate the dot product of subsequences $A_{x}, A_{x+1}, \dots, A_{x+l-1}$ and $B_{y}, B_{y+1}, \dots, B_{y+l-1}$, i.e. the value of the expression
$$\sum_{k=0}^{l-1} A_{x+k} B_{y+k} \,.$$

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains two space-separated integers $N$ and $Q$.
The second line contains $N$ space-separated integers $A_{1}, A_{2}, \dots, A_{N}$.
The third line contains $N$ space-separated integers $B_{1}, B_{2}, \dots, B_{N}$.
Each of the following $Q$ lines contains three space-separated integers $x$, $y$ and $l$ describing one query.

------  Output ------
For each query, print a single line containing one integer — the answer to the query (the dot product).

------  Constraints  ------
$1 ≤ T ≤ 30,000$
$1 ≤ N, Q ≤ 10^{5}$
$1 ≤ A_{i}, B_{i} ≤ 10^{4}$ for each valid $i$
the sum of $N$ for all test cases does not exceed $10^{5}$
the sum of $Q$ for all test cases does not exceed $10^{5}$

----- Sample Input 1 ------ 
1
5 2
4 6 5 2 7
3 2 4 6 3
2 4 2
1 1 1
----- Sample Output 1 ------ 
51
12
"""

import numpy as np

def calculate_dot_product_queries(test_cases):
    results = []
    
    for test_case in test_cases:
        N = test_case['N']
        Q = test_case['Q']
        A = np.array(test_case['A'])
        B = np.array(test_case['B'])
        queries = test_case['queries']
        
        query_results = []
        for x, y, l in queries:
            dot_product = np.dot(A[x - 1:x + l - 1], B[y - 1:y + l - 1])
            query_results.append(dot_product)
        
        results.append(query_results)
    
    return results