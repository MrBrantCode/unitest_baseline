"""
QUESTION:
There is an array contains some non-negative integers. Check whether the array is perfect or not. An array is called perfect if it is first strictly increasing, then constant and finally strictly decreasing. Any of the three parts can be empty.
 
Example 1:
Input : Arr[] = {1, 8, 8, 8, 3, 2}
Output : Yes
Explanation:
We have an array [1, 8, 8, 8, 3, 2]. 
If we look in the range [0, 1] then 
we find that in this range the array is 
increasing, in the range [1, 3] the array 
is constant and in the range [3, 4] the 
array is decreasing.So, it satisfies the above 
condition then we return true.
Example 2:
Input : Arr[] = {1, 1, 2, 2, 1}
Output : No
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function checkUnimodal() that takes an array (arr), sizeOfArray (n), and return bool value that is true if condition satisfied else false. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ a_{i} ≤ 10^{8}
"""

def is_perfect_array(arr, n):
    if n == 1:
        return True
    
    i = 1
    
    # Check for strictly increasing part
    while i < n and arr[i] > arr[i - 1]:
        i += 1
    
    # Check for constant part
    while i < n and arr[i] == arr[i - 1]:
        i += 1
    
    # Check for strictly decreasing part
    while i < n and arr[i] < arr[i - 1]:
        i += 1
    
    # If we have traversed the entire array, it is perfect
    return i == n