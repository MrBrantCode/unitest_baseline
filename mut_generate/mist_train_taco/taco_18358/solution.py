"""
QUESTION:
Given an array of 0s and 1s. Find the length of the largest subarray with equal number of 0s and 1s.
Example 1:
Input:
N = 4
A[] = {0,1,0,1}
Output: 4
Explanation: The array from index [0...3]
contains equal number of 0's and 1's.
Thus maximum length of subarray having
equal number of 0's and 1's is 4.
Example 2:
Input:
N = 5
A[] = {0,0,1,0,0}
Output: 2
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxLen() which takes the array arr[] and the size of the array as inputs and returns the length of the largest subarray with equal number of 0s and 1s.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1 <= N <= 10^{5}
0 <= A[] <= 1
"""

def find_max_length_of_equal_0s_and_1s(arr, N):
    # Replace 0s with -1s
    for i in range(N):
        if arr[i] == 0:
            arr[i] = -1
    
    # Initialize variables
    s = 0
    max_length = 0
    sum_indices = {0: -1}
    
    # Traverse the array
    for i in range(N):
        s += arr[i]
        
        if s in sum_indices:
            max_length = max(max_length, i - sum_indices[s])
        else:
            sum_indices[s] = i
    
    return max_length