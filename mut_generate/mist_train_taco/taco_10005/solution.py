"""
QUESTION:
Given 2 sorted arrays Ar1 and Ar2 of size N each. Merge the given arrays and find the sum of the two middle elements of the merged array.
 
Example 1:
Input:
N = 5
Ar1[] = {1, 2, 4, 6, 10}
Ar2[] = {4, 5, 6, 9, 12}
Output: 11
Explanation: The merged array looks like
{1,2,4,4,5,6,6,9,10,12}. Sum of middle
elements is 11 (5 + 6).
 
Example 2:
Input:
N = 5
Ar1[] = {1, 12, 15, 26, 38}
Ar2[] = {2, 13, 17, 30, 45}
Output: 32
Explanation: The merged array looks like
{1, 2, 12, 13, 15, 17, 26, 30, 38, 45} 
sum of middle elements is 32 (15 + 17).
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function findMidSum() which takes  ar1, ar2 and n as input parameters and returns the sum of middle elements. 
 
Expected Time Complexity: O(log N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{3}
1 <= Ar1[i] <= 10^{6}
1 <= Ar2[i] <= 10^{6}
"""

def find_mid_sum(ar1, ar2, n):
    # Merge the two arrays
    merged_array = sorted(ar1 + ar2)
    
    # Find the middle index
    mid_index = len(merged_array) // 2
    
    # Calculate the sum of the two middle elements
    mid_sum = merged_array[mid_index - 1] + merged_array[mid_index]
    
    return mid_sum