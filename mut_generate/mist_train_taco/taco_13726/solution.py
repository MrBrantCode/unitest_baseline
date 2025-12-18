"""
QUESTION:
Given an array of 0s and 1s, we need to write a program to find the minimum number of swaps required to group all 1s present in the array together.
Example 1:
Input : arr[ ] = {1, 0, 1, 0, 1}
Output : 1
Explanation:
Only 1 swap is required to group all 1's together. 
Swapping index 1 and 4 will give arr[] = {1, 1, 1, 0, 0}.
Example 2:
Input : arr[ ] = {1, 0, 1, 0, 1, 1} 
Output :  1
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function minSwaps() that takes an array (arr), sizeOfArray (n) and return the minimum number of swaps required and if no 1's are present print -1. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N  ≤ 10^{5}
0 ≤ Arr_{i} ≤ 1
"""

def min_swaps_to_group_ones(arr, n):
    K = sum(arr)  # Total number of 1s in the array
    
    if K == 0:
        return -1  # No 1s are present
    
    if K == n:
        return 0  # All elements are 1s, no swaps needed
    
    # Initialize the count of 1s in the first window of size K
    mxones = sum(arr[:K])
    c = mxones
    
    # Sliding window to find the maximum number of 1s in any window of size K
    i = 0
    j = K
    while j < n:
        c += arr[j]  # Add the new element in the window
        c -= arr[i]  # Remove the old element from the window
        mxones = max(mxones, c)
        j += 1
        i += 1
    
    # Minimum swaps required is the total number of 1s minus the maximum 1s in any window of size K
    return K - mxones