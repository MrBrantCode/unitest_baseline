"""
QUESTION:
Given a sorted array arr[] of size N. Find the element that appears only once in the array. All other elements appear exactly twice. 
Example 1:
Input:
N = 11
arr[] = {1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65}
Output: 4
Explanation: 4 is the only element that 
appears exactly once.
 
Your Task:  
You don't need to read input or print anything. Complete the function findOnce() which takes sorted array and its size as its input parameter and returns the element that appears only once. 
Expected Time Complexity: O(log N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
-10^{5} <= arr[i] <= 10^{5}
"""

def find_single_element(arr: list, n: int) -> int:
    """
    Finds the element that appears only once in a sorted array where every other element appears exactly twice.

    Parameters:
    - arr (list): A sorted list of integers.
    - n (int): The size of the list.

    Returns:
    - int: The element that appears only once in the list.
    """
    left, right = 0, n - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Check if mid is even or odd
        if mid % 2 == 1:
            mid -= 1
        
        # If the mid element is equal to the next one, the single element is on the right
        if arr[mid] == arr[mid + 1]:
            left = mid + 2
        else:
            right = mid
    
    return arr[left]