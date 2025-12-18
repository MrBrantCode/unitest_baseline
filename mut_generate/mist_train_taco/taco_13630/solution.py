"""
QUESTION:
Given two sorted arrays and a number x, find the pair whose sum is closest to x and the pair has an element from each array. In the case of multiple closest pairs return any one of them.
Note: The output represents the closest difference of the sum with the number x.
Example 1:
Input : arr[ ] = {1, 4, 5, 7}
brr[ ] = {10, 20, 30, 40} 
X = 32
Output : 1
Explanation:
The closest pair whose sum is closest
to 32 is {1, 30} = 31.
Example 2:
Input : arr[ ] = {1, 4, 5, 7}
brr[ ] = {10, 20, 30, 40}
X = 50 
Output :  3 
Explanation: 
The closest pair whose sum is closest
to 50 is {7, 40} = 47.
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function printClosest() that takes an array (arr), another array (brr), size of array arr (N), size of array brr (M), and return the array of two integers whose sum is closest to X. The driver code takes care of the printing of the closest difference.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N, M ≤ 10^{5}
1 ≤ A[i], B[i] ≤ 10^{7}
"""

def find_closest_pair(arr, brr, x):
    n = len(arr)
    m = len(brr)
    l = 0
    s = m - 1
    diff = float('inf')
    res = []
    
    while l < n and s >= 0:
        current_sum = arr[l] + brr[s]
        current_diff = abs(current_sum - x)
        
        if current_diff < diff:
            diff = current_diff
            res = [arr[l], brr[s]]
        
        if current_sum > x:
            s -= 1
        else:
            l += 1
    
    return res