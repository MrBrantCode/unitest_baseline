"""
QUESTION:
Given a positive integer N, find an array A = [A_{1}, A_{2}, \ldots, A_{N}] of length N consisting of distinct integers from 1 to 10^{9}, such that the following condition is satisfied for each subarray [A_{L}, A_{L+1}, \ldots, A_{r}] (1≤ L ≤ R≤ N):

The sum of elements in the subarray is divisible by its length i.e. A_{L} + A_{L+1} + \ldots + A_{R} is divisible by R - L + 1.

It can be proved that such an array always exists under given constraints.

If there are multiple possible arrays, you may print any of them.

------ Input Format ------ 

- The first line of the input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
- Each test case consists of a single line containing one positive integer N, the length of the array A.

------ Output Format ------ 

For each test case, print one line containing N space-separated integers, the contents of the array A.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ N ≤ 1000$
- Sum of $N$ over all test cases doesn't exceed $5000$

----- Sample Input 1 ------ 
3
1
2
3

----- Sample Output 1 ------ 
1
1 3
4 2 6

----- explanation 1 ------ 
Test case $1$:

For array $A = [1]$,
- The sum of elements of the subarray $[1]$ is equal to $1$ which is divisible by $1$, the length of this subarray.

Test case $2$:

For array $A = [1, 3]$,
- The sum of elements of the subarray $[1]$ is equal to $1$ which is divisible by $1$, the length of this subarray.
- The sum of elements of the subarray $[3]$ is equal to $3$ which is divisible by $1$, the length of this subarray.
- The sum of elements of the subarray $[1, 3]$ is equal to $4$ which is divisible by $2$, the length of this subarray.

Test case $3$:

For array $A = [4, 2, 6]$,
- The sum of elements of the subarray $[4]$ is equal to $4$ which is divisible by $1$, the length of this subarray.
- The sum of elements of the subarray $[2]$ is equal to $2$ which is divisible by $1$, the length of this subarray.
- The sum of elements of the subarray $[6]$ is equal to $6$ which is divisible by $1$, the length of this subarray.
- The sum of elements of the subarray $[4, 2]$ is equal to $6$ which is divisible by $2$, the length of this subarray.
- The sum of elements of the subarray $[2, 6]$ is equal to $8$ which is divisible by $2$, the length of this subarray.
- The sum of elements of the subarray $[4, 2, 6]$ is equal to $12$ which is divisible by $3$, the length of this subarray.
"""

def generate_special_arrays(T, N_list):
    """
    Generates special arrays for each test case where the sum of elements in any subarray is divisible by the length of the subarray.

    Parameters:
    T (int): The number of test cases.
    N_list (list of int): A list of integers where each integer represents the length of the array A for each test case.

    Returns:
    list of list of int: A list of arrays where each array satisfies the given condition.
    """
    result = []
    for k in N_list:
        if k == 1:
            result.append([1])
        elif k % 2 == 0:
            result.append([i for i in range(1, k * 2, 2)])
        else:
            result.append([i for i in range(2, k * 2 + 1, 2)])
    return result