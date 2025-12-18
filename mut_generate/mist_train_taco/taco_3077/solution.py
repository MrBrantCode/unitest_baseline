"""
QUESTION:
Arun has an integer N. His friend likes the number 1, so Arun wants to reduce N to 1.

To do so, he can perform the following move several times (possibly, zero):
Pick two integers X and Y such that X+Y is even and X^{Y} is a divisor of N. Then, replace N by \dfrac{N}{X^{Y}}

Note that at each step, X^{Y} only needs to be a divisor of the *current* value of N, and not necessarily a divisor of the integer Arun initially started with.

Find the minimum number of moves Arun needs to reduce N to 1. If it is not possible to reduce N to 1 using the given operation, print -1 instead.

------ Input Format ------ 

- The first line of input will contain an integer T, denoting the number of test cases. The description of T test cases follows.
- Each test case consists of a single line of input containing one integer N.

------ Output Format ------ 

For each test case, output on a new line the answer — the minimum number of moves needed to reduce N to 1, or -1 if it is not possible to do so.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{18}$

----- Sample Input 1 ------ 
2
25
24

----- Sample Output 1 ------ 
1
-1
----- explanation 1 ------ 
Test case $1$: Choose $X = 25$ and $Y = 1$. $X+Y = 26$ is even, and $X^{Y} = 25$ is a divisor of $N = 25$ so this is a valid choice of $X$ and $Y$. Dividing $N$ by $X^{Y}$ leaves us with $\frac{25}{25} = 1$ and we are done.

Test case $2$: It can be shown that no matter which moves are made, $24$ cannot be reduced to $1$.
"""

def min_moves_to_reduce_to_one(N):
    if N == 1:
        return 0
    
    num2 = 0
    while N % 2 == 0:
        num2 += 1
        N //= 2
    
    if num2 == 0:
        return 1
    elif num2 % 2 == 0 and N != 1:
        ans = 2
        for i in range(2, num2 + 1):
            if num2 % i == 0:
                if (N ** (1 / i)).is_integer() and (2 ** (num2 / i) * N ** (1 / i) + i) % 2 == 0:
                    ans = 1
                    break
        return ans
    elif num2 % 2 == 0 and N == 1:
        return 1
    else:
        return -1