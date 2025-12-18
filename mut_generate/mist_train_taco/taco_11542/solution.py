"""
QUESTION:
Given an array of integers and a number K. Find the count of distinct elements in every window of size K in the array.
Example 1:
Input:
N = 7, K = 4
A[] = {1,2,1,3,4,2,3}
Output: 3 4 4 3
Explanation: Window 1 of size k = 4 is
1 2 1 3. Number of distinct elements in
this window are 3. 
Window 2 of size k = 4 is 2 1 3 4. Number
of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number
of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number
of distinct elements in this window are 3.
Example 2:
Input:
N = 3, K = 2
A[] = {4,1,1}
Output: 2 1
Your Task:
Your task is to complete the function countDistinct() which takes the array A[], the size of the array(N) and the window size(K) as inputs and returns an array containing the count of distinct elements in every contiguous window of size K in the array A[].
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1 <= K <= N <= 10^{5}
1 <= A[i] <= 10^{5 }, for each valid i
"""

def count_distinct_in_windows(A, N, K):
    ans = []
    h = {}
    
    # Initialize the first window
    for i in range(K):
        if A[i] in h:
            h[A[i]] += 1
        else:
            h[A[i]] = 1
    ans.append(len(h))
    
    # Slide the window across the array
    for j in range(1, N - K + 1):
        # Remove the element going out of the window
        if h[A[j - 1]] > 1:
            h[A[j - 1]] -= 1
        else:
            del h[A[j - 1]]
        
        # Add the new element coming into the window
        if A[j + K - 1] in h:
            h[A[j + K - 1]] += 1
        else:
            h[A[j + K - 1]] = 1
        
        # Append the count of distinct elements in the current window
        ans.append(len(h))
    
    return ans