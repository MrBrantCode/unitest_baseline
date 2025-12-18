"""
QUESTION:
GIven two different arrays A and B of size N and M, the task is to merge the two arrays which are unsorted into another array which is sorted.
 
Example 1:
Input: N = 3, M = 3
A[] = {10, 5, 15}
B[] = {20, 3, 2}
Output: 2 3 5 10 15 20
Explanation: After merging both the 
array's and sorting it with get the 
desired output.  
Example 2:
Input: N = 4, M = 3
A[] = {1, 10, 5, 15}
B[] = {20, 0, 2}
Output: 0 1 2 5 10 15 20
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function sortedMerge() that takes array A, array B, array res, integer N, and integer M as parameters and stores merged and sorted array in array res.
 
Expected Time Complexity: O (NlogN + MlogM + (N + M))
Expected Auxiliary Space: O(N+M).
 
Constraints:
1 ≤ N, M ≤ 10^{5}
"""

def merge_and_sort_arrays(A, B):
    # Merge the two arrays
    merged_array = A + B
    
    # Sort the merged array
    merged_array.sort()
    
    return merged_array