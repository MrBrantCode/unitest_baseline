"""
QUESTION:
Given a positive integer N, return the N^{th} row of pascal's triangle.
Pascal's triangle is a triangular array of the binomial coefficients formed by summing up the elements of previous row.
Example :
1
1 1
1 2 1
1 3 3 1
For N = 3, return 3rd row i.e 1 2 1
Example 1:
Input:
N = 4
Output: 1 3 3 1
Explanation: 4^{th} row of pascal's triangle
is 1 3 3 1.
Example 2:
Input:
N = 5
Output: 1 4 6 4 1
Explanation: 5^{th} row of pascal's triangle
is 1 4 6 4 1.
 
Your Task:
Complete the function nthRowOfPascalTriangle() which takes n, as input parameters and returns an array representing the answer. The elements can be large so return it modulo 10^{9} + 7. You don't to print answer or take inputs.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N^{2})
Constraints:
1 ≤ N ≤ 1000
"""

def nth_row_of_pascal_triangle(n):
    MOD = 10**9 + 7
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    prev_row = [1, 1]
    for i in range(3, n + 1):
        current_row = [1] * i
        for j in range(1, i - 1):
            current_row[j] = (prev_row[j - 1] + prev_row[j]) % MOD
        prev_row = current_row
    
    return prev_row