"""
QUESTION:
Given a random set of numbers, Print them in sorted order.
Example 1:
Input:
N = 4
arr[] = {1, 5, 3, 2}
Output: {1, 2, 3, 5}
Explanation: After sorting array will 
be like {1, 2, 3, 5}.
Example 2:
Input:
N = 2
arr[] = {3, 1}
Output: {1, 3}
Explanation: After sorting array will
be like {1, 3}.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function sortArr() which takes the list of integers and the size N as inputs and returns the modified list.
Expected Time Complexity: O(N * log N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N, A[i] ≤ 10^{5}
"""

def sort_array(arr, n):
    """
    Sorts the given list of integers in ascending order.

    Parameters:
    arr (list of int): The list of integers to be sorted.
    n (int): The size of the list.

    Returns:
    list of int: The sorted list of integers.
    """
    arr.sort()
    return arr