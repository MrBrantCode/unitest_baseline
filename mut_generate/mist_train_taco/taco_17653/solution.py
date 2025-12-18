"""
QUESTION:
Given a sorted integer array. We need to make array elements distinct by increasing values and keeping the array sum minimum possible. We need to print the minimum possible sum as output.
Note :- After increasing the values of the array , the sorted order should be maintained.
 
Example 1:
Input : arr[ ] = {2, 2, 3, 5, 6}
Output : 20
Explanation:
We make the array as {2, 3, 4, 5, 6}. 
Sum becomes 2 + 3 + 4 + 5 + 6 = 20
Example 2:
Input : arr[ ] = {20, 20} 
Output :  41
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function minSum() that takes an array (arr), sizeOfArray (n), and return the minimum possible sum. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
2 ≤ N ≤ 10^{5}
1 ≤ A[i] ≤ 10^{5}
"""

def minSum(arr, n):
    for i in range(1, n):
        if arr[i] <= arr[i - 1]:
            arr[i] = arr[i - 1] + 1
    return sum(arr)