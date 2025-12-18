"""
QUESTION:
Given an array A[] of n integers, the task is to find the number of subarrays whose minimal and maximum elements are same.
Example 1:
Input : Arr[] = {1, 1, 3}
Output : 4
Explanation:
The subarrays are
(1), (1), (3) and (1, 1) 
Example 2:
Input : Arr[] = {1, 2, 3, 4}
Output : 4
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function numberOfways() that takes an array (arr), sizeOfArray (n) and return the number of subarrays which follow above condition. The driver code takes care of the printing.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A[i] ≤ 10^{5}
"""

def count_subarrays_with_same_min_max(arr, n):
    output = 1
    count = 1
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            count += 1
        else:
            count = 1
        output += count
    return output