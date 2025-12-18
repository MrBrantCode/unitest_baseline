"""
QUESTION:
Given two binary arrays arr1[] and arr2[] of same size N. Find length of the longest common span [i, j] where j>=i such that arr1[i] + arr1[i+1] + …. + arr1[j] = arr2[i] + arr2[i+1] + …. + arr2[j]. 
 
Example 1:
Input:
N = 6
Arr1[] = {0, 1, 0, 0, 0, 0}
Arr2[] = {1, 0, 1, 0, 0, 1}
Output: 4
Explanation: The longest span with same
sum is from index 1 to 4 following zero 
based indexing.
 
Your Task:
You don't need to read input or print anything. Complete the function longestCommonSum() which takes two arrays arr1, arr2 and integer n as input parameters and returns the length of the longest common span.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 <= N <= 10^{5}
0 <= Arr1[i], Arr2[i] <= 1
"""

def longest_common_sum(arr1, arr2, n):
    # Convert arr1 to the difference array
    for i in range(n):
        arr1[i] = arr1[i] - arr2[i]
    
    # Variables to track prefix sum and answer
    prefix_sum = 0
    hash_map = {}
    max_length = 0
    
    # Iterate through the difference array
    for i in range(n):
        prefix_sum += arr1[i]
        
        # If prefix sum is zero, update max_length
        if prefix_sum == 0:
            max_length = i + 1
        
        # If prefix sum is seen before, update max_length
        if prefix_sum in hash_map:
            max_length = max(max_length, i - hash_map[prefix_sum])
        else:
            hash_map[prefix_sum] = i
    
    return max_length