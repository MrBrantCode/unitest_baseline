"""
QUESTION:
Given a sorted array of size N and an integer K, find the position(0-based indexing) at which K is present in the array using binary search.
Example 1:
Input:
N = 5
arr[] = {1 2 3 4 5} 
K = 4
Output: 3
Explanation: 4 appears at index 3.
Example 2:
Input:
N = 5
arr[] = {11 22 33 44 55} 
K = 445
Output: -1
Explanation: 445 is not present.
Your Task:  
You dont need to read input or print anything. Complete the function binarysearch() which takes arr[], N and K as input parameters and returns the index of K in the array. If K is not present in the array, return -1.
Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(LogN) if solving recursively and O(1) otherwise.
Constraints:
1 <= N <= 10^{5}
1 <= arr[i] <= 10^{6}
1 <= K <= 10^{6}
"""

def binary_search(arr, k):
    """
    Perform binary search on a sorted array to find the index of the element k.

    Parameters:
    arr (list): A sorted list of integers.
    k (int): The integer to search for in the list.

    Returns:
    int: The index of k in the list if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1