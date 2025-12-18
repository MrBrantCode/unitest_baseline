"""
QUESTION:
Given a circular interger array arr of size N (i.e ., the next element of arr [N-1] is arr[0] ), return the next greater number for every element in arr.
The next greater element of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
 
Example 1:
Input:
N = 3
arr[ ] = {1, 2, 1}
Output: {2, -1, 2}
Explanation: The first 1's next greater number is 2:
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:
Input:
N = 5
arr[ ] = {5, 4, 3, 2, 1}
Output: {-1, 5, 5, 5, 5}
Your Task:
You don't need to read input or print anything. Your task is to complete the function nextGreaterElement() which takes the array of integers arr and N as parameters and returns an array of integer which contains the next greater number for every element in arr.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{4}
10^{-9 }≤ arr_{i  }≤ 10^{-9}
"""

def next_greater_elements(arr, N=None):
    if N is None:
        N = len(arr)
    
    ans = [-1] * N
    stack = []
    
    for i in range(2 * N - 1, -1, -1):
        while stack and stack[-1] <= arr[i % N]:
            stack.pop()
        if i < N:
            if stack:
                ans[i] = stack[-1]
            else:
                ans[i] = -1
        stack.append(arr[i % N])
    
    return ans