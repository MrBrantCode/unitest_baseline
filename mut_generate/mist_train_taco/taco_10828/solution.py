"""
QUESTION:
Given an array A[] of size N and a positive integer K, find the first negative integer for each and every window(contiguous subarray) of size K.
 
Example 1:
Input : 
N = 5
A[] = {-8, 2, 3, -6, 10}
K = 2
Output : 
-8 0 -6 -6
Explanation :
First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6
 
Example 2:
Input : 
N = 8
A[] = {12, -1, -7, 8, -15, 30, 16, 28}
K = 3
Output :
-1 -1 -7 -15 -15 0 
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function printFirstNegativeInteger() which takes the array A[], its size N and an integer K as inputs and returns the first negative number in every window of size K starting from the first till the end. If a window does not contain a negative integer , then return 0 for that window.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(K)
Constraints:
1 <= N <= 10^{5}
-10^{5} <= A[i] <= 10^{5}
1 <= K <= N
"""

from collections import deque

def find_first_negative_in_windows(A, N, K):
    result = []
    window_negatives = deque()
    
    # Process the first window
    for i in range(K):
        if A[i] < 0:
            window_negatives.append(i)
    
    # Add the first negative of the first window to the result
    if window_negatives:
        result.append(A[window_negatives[0]])
    else:
        result.append(0)
    
    # Process the remaining windows
    for i in range(K, N):
        # Remove elements from the deque that are not in the current window
        while window_negatives and window_negatives[0] <= i - K:
            window_negatives.popleft()
        
        # Add the current element index to the deque if it's negative
        if A[i] < 0:
            window_negatives.append(i)
        
        # Add the first negative of the current window to the result
        if window_negatives:
            result.append(A[window_negatives[0]])
        else:
            result.append(0)
    
    return result