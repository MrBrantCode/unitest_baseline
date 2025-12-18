"""
QUESTION:
Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element key. The task is to find the index of the given element key in the array A. The whole array A is given as the range to search.
Example 1:
Input:
N = 9
A[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}
key = 10
l = 0 , h = 8
Output:
5
Explanation: 10 is found at index 5.
Example 2:
Input:
N = 4
A[] = {3, 5, 1, 2}
key = 6
l = 0 , h = 3
Output:
-1
Explanation: There is no element that has value 6.
Your Task:
Complete the function search() which takes an array arr[] and start, end index of the array and the K as input parameters, and returns the answer.
Can you solve it in expected time complexity?
Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 10^{7}
0 ≤ A[i] ≤ 10^{8}
1 ≤ key ≤ 10^{8}
"""

def search_rotated_array(A: list, key: int) -> int:
    """
    Searches for the index of the given key in a sorted and rotated array A.

    Parameters:
    - A (list): A sorted and rotated array of distinct integers.
    - key (int): The element to be searched in the array.

    Returns:
    - int: The index of the key in the array A. If the key is not found, returns -1.
    """
    low, high = 0, len(A) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if A[mid] == key:
            return mid
        
        # Check which half is sorted
        if A[low] <= A[mid]:  # Left half is sorted
            if A[low] <= key < A[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # Right half is sorted
            if A[mid] < key <= A[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1