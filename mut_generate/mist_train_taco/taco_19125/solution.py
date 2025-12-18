"""
QUESTION:
You are given two integers N \ ( N ≥ 2) and S. You have to construct an array A containing N integers such that:
0 ≤ A_{i} ≤ S for each 1 ≤ i ≤ N
A_{1} + A_{2} + \ldots + A_{N} = S
A_{1} \mathbin{\&} A_{2} \mathbin{\&} \ldots \mathbin{\&} A_{N} = 0, where \mathbin{\&} denotes [bitwise AND] operator.
The maximum element of the array is minimized.

Find the maximum element of the array A.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- The first and only line of each test case contains two space-separated integers N and S — the length of array and sum of array elements respectively.

------ Output Format ------ 

For each test case, output on a new line the maximum element of the array A.

------ Constraints ------ 

$1 ≤ T ≤ 10^{4}$
$2 ≤ N ≤ 10^{9}$
$1 ≤ S ≤ 10^{9}$

----- Sample Input 1 ------ 
4
2 7
3 6
5 21
100 256455

----- Sample Output 1 ------ 
4
3
5
2570

----- explanation 1 ------ 
Test case $1$: One possible array is $A = [4,3]$. Here $4 +3=7$ and $4 \mathbin{\&} 3=0$. 

Test case $2$: One possible array is $[1, 2, 3]$. Here $1+2+3=6$ and $1 \mathbin{\&} 2 \mathbin{\&} 3=0$. 

Test case $3$: One possible array is $[2, 4, 5,5,5]$. Here $2+4+5+5+5=21$ and $2 \mathbin{\&} 4 \mathbin{\&} 5 \mathbin{\&} 5 \mathbin{\&} 5=0$.
"""

def find_max_element(N: int, S: int) -> int:
    """
    Finds the maximum element of an array A of length N such that:
    1. 0 ≤ A[i] ≤ S for each 1 ≤ i ≤ N
    2. A[1] + A[2] + ... + A[N] = S
    3. A[1] & A[2] & ... & A[N] = 0 (bitwise AND)
    
    The maximum element of the array is minimized.

    Parameters:
    - N (int): The length of the array.
    - S (int): The sum of the array elements.

    Returns:
    - int: The maximum element of the array A.
    """
    X, Y = 0, S + 1
    while X + 1 < Y:
        Mid = X + Y >> 1
        sum = 0
        count = 0
        for j in range(30, -1, -1):
            if Mid >> j & 1:
                sum += (N - 1) * (1 << j)
                count = min(count + 1, N - 1)
            else:
                sum += (1 << j) * count
        if sum >= S:
            Y = Mid
        else:
            X = Mid
    return Y