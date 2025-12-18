"""
QUESTION:
Given an array A[] of N positive integers and two positive integers K_{1} and K_{2}. Find the sum of all elements between K_{1}^{th} and K_{2}^{th} smallest elements of the array. It may be assumed that (1 <= k1 < k2 <= n).
 
Example 1:
Input:
N  = 7
A[] = {20, 8, 22, 4, 12, 10, 14}
K1 = 3, K2 = 6
Output:
26
Explanation:
3rd smallest element is 10
6th smallest element is 20
Element between 10 and 20 
12,14. Their sum = 26.
 
Example 2:
Input
N = 6
A[] = {10, 2, 50, 12, 48, 13}
K1= 2, K2 = 6
Output:
73
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function sumBetweenTwoKth() which takes the array A[], its size N and two integers K1 and K2 as inputs and returns the sum of all the elements between K_{1}^{th} and K_{2}^{th} smallest elements.
 
Expected Time Complexity: O(N. log(N))
Expected Auxiliary Space: O(N)
 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ K_{1}, K_{2} ≤ 10^{9}
"""

def sum_between_two_kth(A, N, K1, K2):
    # Sort the array
    A.sort()
    
    # Extract elements between K1-th and K2-th smallest elements
    elements_between = [x for x in A if A[K1 - 1] < x < A[K2 - 1]]
    
    # Return the sum of these elements
    return sum(elements_between)