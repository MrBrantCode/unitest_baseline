"""
QUESTION:
You are given n numbers a1, a2, ..., an. You can perform at most k operations. For each operation you can multiply one of the numbers by x. We want to make <image> as large as possible, where <image> denotes the bitwise OR. 

Find the maximum possible value of <image> after performing at most k operations optimally.

Input

The first line contains three integers n, k and x (1 ≤ n ≤ 200 000, 1 ≤ k ≤ 10, 2 ≤ x ≤ 8).

The second line contains n integers a1, a2, ..., an (0 ≤ ai ≤ 109).

Output

Output the maximum value of a bitwise OR of sequence elements after performing operations.

Examples

Input

3 1 2
1 1 1


Output

3


Input

4 2 3
1 2 4 8


Output

79

Note

For the first sample, any possible choice of doing one operation will result the same three numbers 1, 1, 2 so the result is <image>. 

For the second sample if we multiply 8 by 3 two times we'll get 72. In this case the numbers will become 1, 2, 4, 72 so the OR value will be 79 and is the largest possible result.
"""

def maximize_bitwise_or(n, k, x, A):
    L = [0] * (n + 1)
    R = [0] * (n + 1)
    
    # Calculate prefix bitwise OR
    for i in range(n):
        L[i + 1] = A[i] | L[i]
    
    # Calculate suffix bitwise OR
    for i in range(n - 1, -1, -1):
        R[i] = A[i] | R[i + 1]
    
    # Calculate the result of multiplying x by k times
    x_power_k = x ** k
    
    # Find the maximum bitwise OR after performing operations
    ans = 0
    for i in range(n):
        ans = max(ans, L[i] | A[i] * x_power_k | R[i + 1])
    
    return ans