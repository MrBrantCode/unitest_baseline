"""
QUESTION:
Chef has an integer N. It is known that the largest [odd] [divisor] of N does not exceed 10^{5}. 

Determine two non-negative integers A and B such that A^{2} + B^{2} = N, or report that no such pair exists.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of a single integer N.

------ Output Format ------ 

For each test case, output space-separated A and B such that A^{2} + B^{2} = N or -1 if no such pair exists.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{15}$
- Largest odd divisor of $N$ won't exceed $10^{5}$.

----- Sample Input 1 ------ 
4
100
6
13
4

----- Sample Output 1 ------ 
8 6
-1
2 3
0 2

----- explanation 1 ------ 
Test case $1$: A possible pair $(A, B)$ such that $A^{2} + B^{2} = N$ is $(8, 6)$. Here, $8^{2} + 6^{2} = 64+36 = 100$.

Test case $2$: There is no pair $(A, B)$ such that $A^{2} + B^{2} = N$.

Test case $3$: A possible pair $(A, B)$ such that $A^{2} + B^{2} = N$ is $(2, 3)$. Here, $2^{2} + 3^{2} = 4+9 = 13$

Test case $4$: A possible pair $(A, B)$ such that $A^{2} + B^{2} = N$ is $(0, 2)$. Here, $0^{2} + 2^{2} = 0+4 = 4$.
"""

import math

def find_pythagorean_pair(N):
    """
    Finds two non-negative integers A and B such that A^2 + B^2 = N, or returns -1 if no such pair exists.

    Parameters:
    N (int): The integer for which to find the Pythagorean pair.

    Returns:
    tuple: A tuple containing two integers (A, B) if a valid pair is found, or (-1,) if no such pair exists.
    """
    MAX = 2 * 10**5
    mul = 1
    
    # Reduce N by dividing by 4 until it is less than or equal to MAX
    while N > MAX:
        N //= 4
        mul *= 2
    
    # Function to find the pair (A, B) such that A^2 + B^2 = n
    def make_square(n):
        a = int(n ** 0.5) // 2
        j = int(n ** 0.5)
        while a <= j:
            temp = n - a * a
            k = temp ** 0.5
            if math.ceil(k) == int(k):
                return (int(k), int(a))
            a += 1
        return (-1,)
    
    res = make_square(N)
    if res == (-1,):
        return (-1,)
    else:
        return (res[0] * mul, res[1] * mul)