"""
QUESTION:
Given a sorted array arr[] of size N without duplicates, and given a value x. Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x. Find the index of K(0-based indexing).
Example 1:
Input:
N = 7, x = 0 
arr[] = {1,2,8,10,11,12,19}
Output: -1
Explanation: No element less 
than 0 is found. So output 
is "-1".
Example 2:
Input:
N = 7, x = 5 
arr[] = {1,2,8,10,11,12,19}
Output: 1
Explanation: Largest Number less than 5 is
2 (i.e K = 2), whose index is 1(0-based 
indexing).
Your Task:
The task is to complete the function findFloor() which returns an integer denoting the index value of K or return -1 if there isn't any such number.
Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 10^{7}
1 ≤ arr[i] ≤ 10^{18}
0 ≤ X ≤^{ }arr[n-1]
"""

def find_floor_index(arr, x):
    """
    Finds the index of the largest element K in the sorted array `arr` such that K is less than or equal to `x`.
    
    Parameters:
    - arr (list of int): A sorted list of integers without duplicates.
    - x (int): The value for which we need to find the floor.
    
    Returns:
    - int: The index of the largest element K in `arr` that is less than or equal to `x`, or -1 if no such element exists.
    """
    n = len(arr)
    if x < arr[0]:
        return -1
    
    low = 0
    high = n - 1
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        else:
            ans = mid
            low = mid + 1
    
    return ans