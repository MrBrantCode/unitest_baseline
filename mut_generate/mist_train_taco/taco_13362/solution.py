"""
QUESTION:
Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.
 
Example 1:
Input:
N = 6
A[] = {3, 2, 1, 56, 10000, 167}
Output:
min = 1, max =  10000
 
Example 2:
Input:
N = 5
A[]  = {1, 345, 234, 21, 56789}
Output:
min = 1, max = 56789
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function getMinMax() which takes the array A[] and its size N as inputs and returns the minimum and maximum element of the array.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
1 <= A_{i} <=10^{12}
"""

def get_min_max(A, N):
    """
    Returns the minimum and maximum elements in the array A.

    Parameters:
    A (list of int): The array of integers.
    N (int): The size of the array.

    Returns:
    tuple: A tuple containing the minimum and maximum elements in the array.
    """
    return (min(A), max(A))