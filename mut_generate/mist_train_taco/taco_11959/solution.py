"""
QUESTION:
Read problem statements in [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

Chef lives in an N \times M grid. He is currently participating in a treasure hunt, and has two items left to find. Chef knows that the Manhattan distance between the cells containing these two items is exactly k. He wants to know, in how many different pairs of cells can the two items be present? 

Let A_{k} be the number of desired pairs when the value of Manhattan distance between the two cells containing these two items is equal to k. Let C = \sum_{i=1}^{N + M - 2} A_{i} \cdot 31^{i-1}. You have to find the value of C.

The answer may be large, so you need to find it modulo 998244353.

The Manhattan distance between two points (x, y) and (x', y') is defined as |x - x'| + |y - y'|. 

------ Input Format ------ 

- The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
- Each testcase contains of a single line of input, two integers N and M.

------ Output Format ------ 

On a new line for each test case, print C modulo 998244353

------ Constraints ------ 

$1 ≤ T ≤ 5$
$1 ≤ N, M ≤ 10^{7}$
- The sum of $N$ over all tests does not exceed $10^{7}$.
- The sum of $M$ over all tests does not exceed $10^{7}$.

------ subtasks ------ 

Subtask #1 (5 points): 
$1 ≤ N, M ≤ 10^{4}$
The sum of $N$ over all tests does not exceed $10^{4}$.
The sum of $M$ over all tests does not exceed $10^{4}$.

Subtask #2 (35 points): 
$1 ≤ N, M ≤ 10^{6}$
The sum of $N$ over all tests does not exceed $10^{6}$.
The sum of $M$ over all tests does not exceed $10^{6}$.

Subtask #3 (60 points): original constraints

----- Sample Input 1 ------ 
3
2 3
2 4
100 350
----- Sample Output 1 ------ 
2115
65668
895852507
----- explanation 1 ------ 

Test case $1$:  
The pairs of points with distance $1$ are:
- $(1, 1)$ and $(1, 2)$
- $(1, 1)$ and $(2, 1)$
- $(1, 2)$ and $(1, 3)$
- $(1, 2)$ and $(2, 2)$
- $(1, 3)$ and $(2, 3)$
- $(2, 1)$ and $(2, 2)$
- $(2, 2)$ and $(2, 3)$

The pairs of points with distance $2$ are:
- $(1, 1)$ and $(1, 3)$
- $(1, 1)$ and $(2, 2)$
- $(1, 2)$ and $(2, 3)$
- $(1, 2)$ and $(2, 1)$
- $(1, 3)$ and $(2, 2)$
- $(2, 1)$ and $(2, 3)$

The pairs of points with distance $3$ are:
- $(1, 1)$ and $(2, 3)$
- $(2, 1)$ and $(1, 3)$

Therefore, the answer is $7 \cdot 31^{0} + 6 \cdot 31^{1} + 2 \cdot 31^{2}$ = $2115$.
"""

def calculate_treasure_hunt_value(T, test_cases):
    mdval = 998244353
    tlst31 = [0, 1]
    t2li = []
    (fval, sval, t2val) = (2, 2, 4)
    
    results = []
    
    for (n, m) in test_cases:
        mulmn = 2 * m * n
        addmn = m + n
        nm2 = n + m - 2
        c2len = n + m - 2 - max(n, m)
        ntlilen = len(tlst31)
        n2len = len(t2li)
        lsval = tlst31[-1]
        
        if ntlilen < nm2:
            for _ in range(ntlilen, nm2 + 3):
                lsval = lsval * 31 % mdval
                tlst31.append(lsval)
        
        if n2len < c2len:
            for _ in range(n2len, c2len + 2):
                t2li.append(fval)
                sval += t2val
                fval += sval
                t2val += 2
        
        ans = 0
        mn1 = 6 * m * n - 1
        tnpm = 3 * (n + m)
        npm = tnpm
        (b2, bsval) = (1, 3)
        
        for b in range(1, min(n, m) + 1):
            tval = b * (mn1 + b2 - npm) // 3
            npm += tnpm
            b2 += bsval
            bsval += 2
            ans = (ans + tlst31[b] * tval) % mdval
        
        mival = min(n, m)
        sqval = mival * mival % mdval
        
        for i in range(min(n, m) + 1, max(n, m) + 1):
            tval = tval - sqval
            ans = (ans + tlst31[i] * tval) % mdval
        
        ixval = n + m - 2
        ix2 = 0
        
        for i in range(max(n, m) + 1, n + m - 1):
            ans = (ans + tlst31[ixval] * t2li[ix2]) % mdval
            ix2 += 1
            ixval -= 1
        
        results.append(ans)
    
    return results