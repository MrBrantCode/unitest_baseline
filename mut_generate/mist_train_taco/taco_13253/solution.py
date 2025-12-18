"""
QUESTION:
Given A, B and N. Find x and y that satisfies equation Ax + By = N. If there's no solution print -1 in place of both x and y. 
Note: There are Multiple solutions possible. Find the solution where x is minimum. x and y should both be non-negative.
 
Example 1:
Input:
A = 2, B = 3, N = 7
Output:
2 1
Explanation:
2*2 + 3*1 = 7.
Example 2:
Input:
A = 4, B = 2, N = 7
Output:
-1 -1
Explanation:
There's no solution for x and y the equation.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function findXandY() which takes 3 Integers A,B and N as input and returns a list of 2 integers with the first integer x and the second being y.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= A,B <= 10^{5}
0 <= N <= 10^{5}
"""

def find_min_x_y(A, B, N):
    # Check if N is divisible by B
    if N % B == 0:
        return [0, N // B]
    
    # Iterate to find the minimum x
    for i in range(1, N):
        c = N - A * i
        if c > 0 and c % B == 0:
            return [i, c // B]
    
    # If no solution is found, return [-1, -1]
    return [-1, -1]