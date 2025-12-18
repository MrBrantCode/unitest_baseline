"""
QUESTION:
Chef loves problems about digits and he came up with an interesting one.

Chef has given you two integers N and K. You should find the minimum non-negative integer X, such that N + X has at most K distinct digits in its decimal representation.

For example, 1231 has three distinct digits and 100 has two distinct digits.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- The first and only line of each test case consists of two space-separated integers N and K, as described in the problem statement.

------ Output Format ------ 

For each test case, output on a new line the minimum non-negative integer X which satisfies the problem conditions.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{9}$
$1 ≤ K ≤ 10$

----- Sample Input 1 ------ 
9
30 1
56 4
364 2
125 3
37662730 3
41872528 4
73170084 8
90032975 1
7487471 3
----- Sample Output 1 ------ 
3
0
2
0
603
1583
0
9967024
3
----- explanation 1 ------ 
Test case $1$: $30$ has $2$ distinct digits which is more than $1$, so we should add $3$ to $30$ to make it equal to $33$ which has only $1$ distinct digit.
"""

def find_min_increment(N: int, K: int) -> int:
    n_str = str(N)
    n_digits = list(map(int, n_str))
    
    if len(set(n_digits)) <= K:
        return 0
    
    for i, d in enumerate(n_digits):
        if d == 9:
            continue
        
        used_digits = set(n_digits[:i])
        
        if len(used_digits) > K:
            break
        
        if len(used_digits) < K:
            d1 = d + 1
            used_digits.add(d1)
        else:
            d1 = d + 1
            while d1 not in used_digits and d1 != 10:
                d1 += 1
            if d1 == 10:
                continue
        
        if len(used_digits) == K:
            d2 = min(used_digits)
        else:
            d2 = 0
        
        modified_digits = n_digits.copy()
        modified_digits[i] = d1
        for j in range(i + 1, len(n_digits)):
            modified_digits[j] = d2
        
        acc = 0
        for x in modified_digits:
            acc = 10 * acc + x
        
        return acc - N
    
    return 0  # Fallback, should not reach here given constraints