"""
QUESTION:
Let's consider a permutation P = {$p_{1}$,$ p_{2}$, ..., $p_{N}$} of the set of N = {1, 2, 3, ..., N} elements .  

P is called a magic set if it satisfies both of the following constraints:  

Given a set of K integers, the elements in positions $a_{1}$, $a_{2}$, ..., $a_{K}$ are less than their adjacent elements, i.e., $p_{ai-1} > p_{ai} < p_{ai+1}$
Given a set of L integers, elements in positions $b_{1}$, $b_{2}$, ..., $b_{L}$ are  greater than their adjacent elements, i.e., $p_{bi-1} < p_{bi} > p_{bi+1}$

How many such magic sets are there?

Input Format 

The first line of input contains three integers N, K, L separated by a single space. 

The second line contains K integers, $a_{1}$, $a_{2$}, ... $a_{K}$ each separated by single space. 

the third line contains L integers, $b_{1}$, $b_{2}$, ... $b_{L}$ each separated by single space. 

Output Format 

Output the answer modulo 1000000007 (10^{9}+7).

Constraints 

3 <= N <= 5000 

1 <= K, L <= 5000 

2 <= $a_{i}$, $b_{j}$ <= N-1, where i ∈ [1, K] AND j ∈ [1, L]  

Sample Input #00  

4 1 1
2
3

Sample Output #00  

5

Explanation #00

Here, N = 4 $a_{1}$ = 2 and $b_{1}$ = 3. The 5 permutations of {1,2,3,4} that satisfy the condition are 

2 1 4 3
3 2 4 1
4 2 3 1
3 1 4 2
4 1 3 2

Sample Input #01

10 2 2
2 4
3 9

Sample Output #01

161280
"""

def count_magic_sets(N, K, L, K_indices, L_indices):
    M = 10 ** 9 + 7
    K_indices = set(K_indices)
    L_indices = set(L_indices)
    
    done = False
    if len(K_indices & L_indices) > 0:
        done = True
    
    (Q_12, Q_22) = (0, 0)
    if 2 in K_indices:
        Q_12 = 1
        Q_22 = 0
    elif 2 in L_indices:
        Q_12 = 0
        Q_22 = 1
    else:
        Q_12 = 1
        Q_22 = 1
    
    prev_Q_partials = {}
    prev_Q_partials[0] = 0
    prev_Q_partials[1] = Q_12
    prev_Q_partials[2] = Q_12 + Q_22
    
    for j in range(3, N + 1):
        current_Q_partials = {}
        current_Q_partials[0] = 0
        for i in range(1, j + 1):
            if j in K_indices:
                Q_ij = 0
                if j - 1 in K_indices:
                    done = True
                    break
                else:
                    Q_ij = (prev_Q_partials[j - 1] - prev_Q_partials[i - 1]) % M
            elif j in L_indices:
                if j - 1 in L_indices:
                    done = True
                    break
                Q_ij = prev_Q_partials[i - 1] % M
            elif j - 1 in K_indices:
                Q_ij = prev_Q_partials[i - 1] % M
            elif j - 1 in L_indices:
                Q_ij = (prev_Q_partials[j - 1] - prev_Q_partials[i - 1]) % M
            else:
                Q_ij = prev_Q_partials[j - 1] % M
            current_Q_partials[i] = (current_Q_partials[i - 1] + Q_ij) % M
        prev_Q_partials = current_Q_partials
        if done:
            break
    
    if done:
        return 0
    else:
        return current_Q_partials[N] % M