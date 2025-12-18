"""
QUESTION:
Given a binary array A[] of size N. The task is to arrange the array in increasing order.
Note: The binary array contains only 0  and 1.
 
Example 1:
Input: 
5
1 0 1 1 0
Output: 
0 0 1 1 1
Explanation: 
After arranging the elements in 
increasing order, elements will be as 
0 0 1 1 1.
Example 2:
Input:
10
1 0 1 1 1 1 1 0 0 0
Output: 
0 0 0 0 1 1 1 1 1 1
Explanation: 
After arranging the elements in 
increasing order, elements will be 
0 0 0 0 1 1 1 1 1 1.
Your Task: This is a function problem. You only need to complete the function binSort() that takes the array A[] and it's size N as parameters and sorts the array. The printing is done automatically by the driver code.
Expected Time Complexity: O(N)
Expected Auxilliary Space: O(1)
Constraints:
1 <= N <= 10^{6}
0 <= A[i] <= 1
"""

def sort_binary_array(A, N):
    """
    Sorts a binary array A of size N in increasing order.

    Parameters:
    A (list of int): The binary array containing only 0s and 1s.
    N (int): The size of the array.

    Returns:
    list of int: The sorted binary array.
    """
    # Count the number of 0s
    count_zeros = A.count(0)
    
    # Fill the first 'count_zeros' elements with 0s and the rest with 1s
    A[:count_zeros] = [0] * count_zeros
    A[count_zeros:] = [1] * (N - count_zeros)
    
    return A