"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

Chef wants to give a gift to Chefina to celebrate their anniversary. Of course, he has a sequence $a_{1}, a_{2}, \ldots, a_{N}$ ready for this occasion. Since the half-heart necklace is kind of cliche, he decided to cut his sequence into two pieces and give her a piece instead. Formally, he wants to choose an integer $l$ ($1 ≤ l < N$) and split the sequence into its prefix with length $l$ and its suffix with length $N-l$.

Chef wants his gift to be *cute*; he thinks that it will be cute if the product of the elements in Chefina's piece is coprime with the product of the elements in his piece. Can you tell him where to cut the sequence? Find the smallest valid $l$ such that Chef's gift would be cute.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains the integer $N$.
The second line contains $N$ space-separated integers $a_{1}, a_{2}, \ldots, a_{N}$.

------  Output ------
For each test case, print a single line containing one integer $l$ where Chef should cut the sequence.

It is guaranteed that a solution exists for the given test data.

------  Constraints ------
$1 ≤ T ≤ 20$
$2 ≤ N ≤ 10^{5}$
$2 ≤ a_{i} ≤ 10^{5}$ for each valid $i$
the sum of $N$ over all test cases does not exceed $3 \cdot 10^{5}$

------  Subtasks ------
Subtask #1 (25 points):
$N ≤ 200$
the sum of $N$ over all test cases does not exceed $600$

Subtask #2 (40 points):
$N ≤ 2,000$
the sum of $N$ over all test cases does not exceed $6,000$

Subtask #3 (35 points): original constraints

----- Sample Input 1 ------ 
1

4

2 3 4 5
----- Sample Output 1 ------ 
3
"""

def find_cut_position(test_cases):
    N = 100000
    prime = [-1 for i in range(N + 1)]
    i = 2
    while i <= N:
        if prime[i] == -1:
            prime[i] = i
            for j in range(2 * i, N + 1, i):
                if prime[j] == -1:
                    prime[j] = i
        i += 1
    
    results = []
    
    for case in test_cases:
        n, arr = case
        range_p = [[-1, -1] for i in range(N + 1)]
        
        for i in range(n):
            a = arr[i]
            while a > 1:
                x = prime[a]
                if range_p[x][0] == -1:
                    range_p[x][0] = i
                    range_p[x][1] = i
                else:
                    range_p[x][1] = i
                a = a // x
        
        mark = [0 for i in range(n)]
        for i in range(2, N + 1):
            if range_p[i][0] != -1:
                l = range_p[i][0]
                r = range_p[i][1]
                mark[l] += 1
                mark[r] -= 1
        
        for i in range(1, n):
            mark[i] += mark[i - 1]
        
        for i in range(n):
            if mark[i] == 0:
                results.append(i + 1)
                break
    
    return results