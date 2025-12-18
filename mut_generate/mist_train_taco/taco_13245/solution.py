"""
QUESTION:
Initially, Chef is at coordinate 0 on X-axis. For each i = 1, 2, \dots, N in order, Chef does the following:
If Chef is at a non-negative coordinate, he moves i steps backward (i.e, his position's coordinate decreases by i), otherwise he moves i steps forward (i.e, his position's coordinate increases by i). 

You are given the integer N. Find the final position of Chef on the X-axis after N operations.

------ Input Format ------ 

- The first line of input contains an integer T, denoting the number of test cases. The T test cases then follow:
- The first and only line of each test case contains an integer N.

------ Output Format ------ 

For each test case, output in a single line the final position of Chef on the X-axis after N operations.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{9}$

----- Sample Input 1 ------ 
3
1
2
3

----- Sample Output 1 ------ 
-1
1
-2

----- explanation 1 ------ 
Test case $1$: Initially, Chef is at coordinate $0$ on X-axis. As $0$ is non-negative, during the first operation Chef moves $1$ step backward and reaches the coordinate $-1$.

Test case $2$: Chef is at coordinate $-1$ on X-axis after the first operation. As $-1$ is negative, during the second operation Chef moves $2$ steps forward and reaches the coordinate $1$.
"""

def calculate_final_position(N: int) -> int:
    """
    Calculate the final position of Chef on the X-axis after N operations.

    Parameters:
    N (int): The number of operations Chef will perform.

    Returns:
    int: The final position of Chef on the X-axis.
    """
    ans = N / 2
    ans1 = N // 2
    a = -(ans1 + 1)
    if ans > ans1:
        return a
    else:
        return ans1