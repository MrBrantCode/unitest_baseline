"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Consider an ordered tree with N vertices. Your task is to calculate the expected value of the number of vertices having exactly one child in such tree assuming that it is uniformly chosen from the set of all ordered trees of size N. 

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows. 

Each testcase contains a single integer N for which you should calculate the answer.

------ Output ------ 

For each test case, output a single line containing two integers, which are explained below.
Consider the answer to be a proper fraction P/Q, where gcd(P, Q) = 1. Then your task is to output two integers PQ^{-1} mod 10^{9}+7 and PQ^{-1} mod 10^{9}+9.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$It is guaranteed that Q will be invertible with respect to both the modulos.$

------ Subtasks ------ 

Subtask #1 (10 points)

$1 ≤ N ≤ 10^{3}$

Subtask #2 (20 points)

$1 ≤ N ≤ 10^{6}$

Subtask #3 (30 points)

$1 ≤ N ≤ 10^{9}$

Subtask #4 (40 points)

$1 ≤ N ≤ 10^{18}$

----- Sample Input 1 ------ 
4

1

2

3

4
----- Sample Output 1 ------ 
0 0

1 1

1 1

400000004 200000003
----- explanation 1 ------ 
You can see every possible tree with 1, 2, 3 or 4 vertices on the diagram below.

From this you can see that answers for these inputs are 0/1 = 0, 1/1 = 1, (2+0)/2 = 1 and (3+1+1+1+0)/5 = 6/5 correspondingly.
"""

def calculate_expected_vertices(n, mod1=1000000007, mod2=1000000009):
    """
    Calculate the expected value of the number of vertices having exactly one child in an ordered tree with n vertices.

    Parameters:
    n (int): The number of vertices in the tree.
    mod1 (int): The first modulo value (default is 10^9 + 7).
    mod2 (int): The second modulo value (default is 10^9 + 9).

    Returns:
    tuple: A tuple containing two integers (result1, result2) where:
           - result1 is the result modulo mod1.
           - result2 is the result modulo mod2.
    """
    
    def pow1(a, b, mod):
        a %= mod
        if b == 0:
            return 1
        res = pow1(a, b // 2, mod)
        res *= res
        res %= mod
        if b % 2:
            res *= a
        return res % mod
    
    if n == 1:
        return (0, 0)
    
    if n <= 3:
        return (1, 1)
    
    p1 = n * (n - 1) % mod1
    p2 = n * (n - 1) % mod2
    q1 = 2 * (n + n - 3) % mod1
    q2 = 2 * (n + n - 3) % mod2
    
    inv1 = pow1(q1, mod1 - 2, mod1)
    inv2 = pow1(q2, mod2 - 2, mod2)
    
    ans1 = p1 * inv1 % mod1
    ans2 = p2 * inv2 % mod2
    
    return (ans1, ans2)