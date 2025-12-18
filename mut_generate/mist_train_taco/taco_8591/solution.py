"""
QUESTION:
Given an integer array arr of size N. The Range of a subarray of arr is the difference between the largest and smaller element in the subarray.  
Return the sum of all subarray ranges of arr.
Example 1:
Input:
N = 3
arr[ ] = {1, 2, 3}
Output: 4
Explanation: The 6 subarrays of arr are the following :
{1 } , range = largest - smallest = 1 - 1 = 0 
{2 } , range = 2 - 2 = 0
{3 } , range = 3 - 3 = 0
{1, 2}, range = 2 - 1 = 1
{2, 3}, range = 3 - 2 = 1
{1, 2, 3}, range = 3 - 1 = 2
sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4
 
Example 2:
Input:
N = 4
arr[ ] = {-32, 0, -2, 72}
Output: 318
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function subarrayRanges() which takes the array of integers arr and N as parameters and returns a sum of all subarrays ranges of arr.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{3}
10^{-9 }≤ arr_{i  }≤ 10^{-9}
"""

def subarray_ranges_sum(arr, N):
    res = 0
    min_stack, max_stack = [], []
    n = len(arr)
    arr.append(0)  # Append a sentinel value to handle the last element
    
    for i, num in enumerate(arr):
        while min_stack and (i == n or num < arr[min_stack[-1]]):
            top = min_stack.pop()
            starts = top - min_stack[-1] if min_stack else top + 1
            ends = i - top
            res -= starts * ends * arr[top]
        min_stack.append(i)
        
        while max_stack and (i == n or num > arr[max_stack[-1]]):
            top = max_stack.pop()
            starts = top - max_stack[-1] if max_stack else top + 1
            ends = i - top
            res += starts * ends * arr[top]
        max_stack.append(i)
    
    return res