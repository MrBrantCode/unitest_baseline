"""
QUESTION:
Given an unsorted array arr[] of size N. Rotate the array to the left (counter-clockwise direction) by D steps, where D is a positive integer. 
 
Example 1:
Input:
N = 5, D = 2
arr[] = {1,2,3,4,5}
Output: 3 4 5 1 2
Explanation: 1 2 3 4 5  when rotated
by 2 elements, it becomes 3 4 5 1 2.
Example 2:
Input:
N = 10, D = 3
arr[] = {2,4,6,8,10,12,14,16,18,20}
Output: 8 10 12 14 16 18 20 2 4 6
Explanation: 2 4 6 8 10 12 14 16 18 20 
when rotated by 3 elements, it becomes 
8 10 12 14 16 18 20 2 4 6.
 
Your Task:
Complete the function rotateArr() which takes the array, D and N as input parameters and rotates the array by D elements. The array must be modified in-place without using extra space. 
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{6}
1 <= D <= 10^{6}
0 <= arr[i] <= 10^{5}
"""

def rotate_array(arr, D, N):
    """
    Rotates the given array to the left by D steps.

    Parameters:
    arr (list): The input array to be rotated.
    D (int): The number of steps to rotate the array to the left.
    N (int): The size of the array.

    Returns:
    None: The array is modified in-place.
    """
    D = D % N  # Normalize D to be within the range of the array length
    if D == 0:
        return  # No need to rotate if D is a multiple of N
    
    # Store the first D elements in a temporary list
    temp = arr[:D]
    
    # Shift the remaining elements to the left by D positions
    for i in range(D, N):
        arr[i - D] = arr[i]
    
    # Place the stored elements at the end of the array
    for i in range(N - D, N):
        arr[i] = temp[i - (N - D)]