"""
QUESTION:
Given a sorted array Arr[](0-index based) consisting of N distinct integers and an integer k, the task is to find the index of k, if its present in the array Arr[]. Otherwise, find the index where k must be inserted to keep the array sorted.
Example 1:
Input:
N = 4
Arr = {1, 3, 5, 6}
k = 5
Output: 2
Explaination: Since 5 is found at index 2 
as Arr[2] = 5, the output is 2.
Example 2:
Input:
N = 4
Arr = {1, 3, 5, 6}
k = 2
Output: 1
Explaination: Since 2 is not present in 
the array but can be inserted at index 1 
to make the array sorted.
Your Task:
You don't need to read input or print anything. Your task is to complete the function searchInsertK() which takes the array Arr[] and its size N and k as input parameters and returns the index.
Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{4}
-10^{3} ≤ Arr[i] ≤ 10^{3}
-10^{3} ≤ k ≤ 10^{3}
"""

from bisect import bisect_left

def search_insert_position(Arr, k):
    """
    Finds the index of the integer k in the sorted array Arr.
    If k is not present, returns the index where k should be inserted to keep the array sorted.

    Parameters:
    Arr (list of int): A sorted list of distinct integers.
    k (int): The integer to search for or insert.

    Returns:
    int: The index of k in Arr, or the index where k should be inserted.
    """
    return bisect_left(Arr, k)