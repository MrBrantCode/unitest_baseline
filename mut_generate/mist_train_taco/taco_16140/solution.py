"""
QUESTION:
Given an array of N positive integers. The task is to find maximum value of |A[i] – A[j]| + |i – j|, where 0 <= i, j <= N – 1 and A[i], A[j] belong to the array.
 
Example 1:
Input : 
N = 4
A[] = { 1, 2, 3, 1 }
Output :
4
Explanation:
Choose i = 0 and j = 4
 
Example 2:
Input :
N = 3 
A[] = { 1, 1, 1 }
Output : 
2
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function maxValueOfExpression() which takes the array A[] and its size N as inputs and returns the maximum value of expression in array A[].
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
1 <= A[i] <= 10^{5}
"""

def max_value_of_expression(A, N):
    case1 = [0] * N
    case2 = [0] * N
    
    for i in range(N):
        case1[i] = A[i] + i
        case2[i] = A[i] - i
    
    res1 = abs(max(case1) - min(case1))
    res2 = abs(max(case2) - min(case2))
    
    return max(res1, res2)