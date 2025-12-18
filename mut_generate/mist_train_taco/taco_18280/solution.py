"""
QUESTION:
Given an array of integers (A[])  and a number x, find the smallest subarray with sum greater than the given value. If such a subarray do not exist return 0 in that case.
Note: The answer always exists. It is guaranteed that x doesn't exceed the summation of a[i] (from 1 to N).
Example 1:
Input:
A[] = {1, 4, 45, 6, 0, 19}
x  =  51
Output: 3
Explanation:
Minimum length subarray is 
{4, 45, 6}
Example 2:
Input:
A[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Explanation:
Minimum length subarray is {10}
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function smallestSubWithSum() which takes the array A[], its size N and an integer X as inputs and returns the required ouput.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N, x ≤ 10^{5}
1 ≤ A[] ≤ 10^{4}
"""

def smallest_subarray_with_sum(A, x):
    n = len(A)
    start = 0
    end = 0
    current_sum = 0
    min_length = n + 1

    while end < n:
        while current_sum <= x and end < n:
            current_sum += A[end]
            end += 1

        while current_sum > x and start < n:
            min_length = min(min_length, end - start)
            current_sum -= A[start]
            start += 1

    return min_length if min_length != n + 1 else 0