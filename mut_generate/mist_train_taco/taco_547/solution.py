"""
QUESTION:
Given an array arr of size N with all initial values as 0, the task is to perform the following M range increment operations as shown below: 
Increment(a_{i}, b_{i}, k_{i}) : Increment values from index 'a_{i}' to 'b_{i}' by 'k_{i}'.
After M operations, calculate the maximum value in the array arr[].
Example 1:
Input: N = 5, M = 3, a[] = {0, 1, 2}
b[] = {1, 4, 3}, k[] = {100, 100, 100}
Output: 200
Explanation: Initially array = {0, 0, 0, 
                                   0, 0}
After first operation : {100, 100, 0, 0, 0}
After second operation: {100, 200, 100, 100, 100}
After third operation: {100, 200, 200, 200, 100}
Maximum element after m operations is 200.
Example 2:
Input: N = 4, M = 3, a[] = {1, 0, 3} 
b[] = {2, 0, 3}, k[] = {603, 286, 882}
Output: 882
Explanation: Initially array = {0, 0, 0, 0}
After first operation: {0, 603, 603, 0}
After second operation: {286, 603, 603, 0}
After third operation: {286, 603, 603, 882}
Maximum element after m operations is 882.
Your Task:
You don't need to read input or print anything. You just need to complete the function findMax() that takes arrays a[], b[], k[] and integers N, M as parameters and returns the desired output.
 
Expected Time Complexity: O(M+N).
Expected Auxiliary Space: O(N).
 
Constraints:
1 ≤ N ≤ 10^{6}
0 ≤ a_{i } ≤ b_{i} ≤ N-1
1 ≤ M ≤ 10^{6}
0 ≤ k_{i} ≤ 10^{6}
"""

def find_max_value_after_operations(N, M, a, b, k):
    # Initialize the array with zeros
    ans = [0] * (N + 1)
    
    # Apply the range increments
    for i in range(M):
        ans[a[i]] += k[i]
        if b[i] + 1 < N + 1:
            ans[b[i] + 1] -= k[i]
    
    # Calculate the prefix sums to get the final values in the array
    for i in range(1, N + 1):
        ans[i] += ans[i - 1]
    
    # Return the maximum value in the array
    return max(ans[:N])