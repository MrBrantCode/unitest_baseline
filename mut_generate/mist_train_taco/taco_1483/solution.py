"""
QUESTION:
Chef has an integer N. He repeats the following operation until N becomes 1.

- Chef chooses an integer X such that X > 1 and X is a divisor of N and then divides N by X (the new value of N becomes N/X). If X is even, Chef gets A points otherwise he gets B points

Can you find the maximum points Chef can get if he performs the operations optimally?

------ Input Format ------ 

- First line will contain T, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input containing three integers N, A, B.

------ Output Format ------ 

For each testcase, output in a single line the maximum points Chef can get.

------ Constraints ------ 

$1 ≤ T ≤ 2\cdot10^{3}$
$2 ≤ N ≤ 10^{9}$
$-10^{3}≤ A, B ≤ 10^{3}$

----- Sample Input 1 ------ 
4
10 2 3
15 5 -2
12 2 3
8 -1 0

----- Sample Output 1 ------ 
5
-2
7
-1

----- explanation 1 ------ 
Test case $1$: First Chef divides $N = 10$ by $2$ and gets $2$ points and then divides by $5$ and thus gets $3$ points. Hence Chef gets a total of $2 + 3 = 5$ points.

Test case $2$: Chef divides $N$ by $15$. Hence he gets $-2$ points.
"""

def calculate_max_points(N, A, B):
    """
    Calculate the maximum points Chef can get by optimally dividing N by its divisors.

    Parameters:
    N (int): The initial integer value.
    A (int): Points gained for dividing by an even divisor.
    B (int): Points gained for dividing by an odd divisor.

    Returns:
    int: The maximum points Chef can get.
    """
    def snek(n):
        even = 0
        odd = 0
        while n % 2 == 0:
            n //= 2
            even += 1
        for j in range(3, int(n ** 0.5) + 1, 2):
            if n % j == 0:
                while n % j == 0:
                    n //= j
                    odd += 1
        if n != 1:
            odd += 1
        return [even, odd]
    
    ans = snek(N)
    if A < 0 and B < 0:
        if N % 2 == 0:
            return A
        else:
            return B
    elif A < 0 and B >= 0:
        if ans[0] > 0:
            return ans[1] * B + A
        else:
            return ans[1] * B
    elif A >= 0 and B < 0:
        if ans[0] > 0:
            return ans[0] * A
        else:
            return B
    else:
        return ans[0] * A + ans[1] * B