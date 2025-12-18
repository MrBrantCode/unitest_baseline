"""
QUESTION:
Read problem statements in [Mandarin Chinese] and [Vietnamese] as well.

Chef placed $N$ boxes (numbered $1$ through $N$) in a straight line. For each valid $i$, the $i$-th box contains $A_{i}$ balls. 

Then, Chef painted the boxes using $M$ distinct colours in such a way that for each $M$ consecutive boxes, no two of these boxes have the same colour.

Help Chef choose $M$ distinct boxes (not necessarily consecutive) such that no two of the chosen boxes have the same colour and the difference between the number of balls in a box that contains the maximum number of balls and a box that contains the minimum number of balls among the chosen boxes is the smallest possible.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains two space-separated integers $N$ and $M$.
The second line contains $N$ space-separated integers $A_{1}, A_{2}, \ldots, A_{N}$.

------  Output ------
For each test case, print a single line containing one integer ― the minimum possible difference between the maximum and minimum number of balls in the chosen boxes.

------  Constraints ------
$1 ≤ T ≤ 5$
$2 ≤ M ≤ N ≤ 10^{5}$
$1 ≤ A_{i} ≤ 10^{9}$, for each valid $i$

------  Subtasks ------
Subtask #1 (30 points): $N ≤ 10^{3}$

Subtask #2 (70 points): original constraints

----- Sample Input 1 ------ 
1   

4 2  

10 20 15 28
----- Sample Output 1 ------ 
5
----- explanation 1 ------ 
Example case 1: Let's denote the colours by 'R' (red) and 'G' (green). There are two possible ways of painting the boxes: "RGRG" and  "GRGR".

There are four ways to choose two boxes (one red and one green box). The numbers of balls in them and the differences are:
- $(10, 28)$ with difference $28-10=18$
- $(10, 20)$ with difference $20-10=10$
- $(15, 28)$ with difference $28-15=13$
- $(15, 20)$ with difference $20-15=5$, which is the smallest possible
"""

def find_min_ball_difference(test_cases):
    results = []
    
    for case in test_cases:
        N, M, A = case
        l = []
        c = [0] * M
        f = 0
        r = 0
        result = 10 ** 10
        
        for i in range(N):
            l2 = [A[i], i % M]
            l.append(l2)
        
        l.sort()
        
        for i in range(N):
            while r < N and f < M:
                if c[l[r][1]] == 0:
                    f += 1
                c[l[r][1]] += 1
                r += 1
            
            if f == M:
                result = min(result, l[r - 1][0] - l[i][0])
            
            c[l[i][1]] -= 1
            if c[l[i][1]] == 0:
                f -= 1
        
        results.append(result)
    
    return results