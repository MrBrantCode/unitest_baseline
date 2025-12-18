"""
QUESTION:
Given an array A of n integers, find the sum of f(a[i], a[j]) of all pairs (i, j) such that (1 <= i < j <= n).
f(a[i], a[j]):       if abs(a[j]-a[i]) > 1
                         f(a[i], a[j]) = a[j] - a[i]
                         else  if abs(a[j]-a[i]) <= 1
                         f(a[i], a[j]) = 0 
Example 1:
Input : arr[ ] = {6, 6, 4, 4}
Output : -8
Explanation:
All pairs are: 
(6 - 6) + (4 - 6) + (4 - 6) + 
(4 - 6) + (4 - 6) + (4 - 4) = -8
return -8.
Example 2:
Input : arr[ ] = {1, 2, 3, 1, 3} 
Output:  4
Explanation: All pairs are:
(3-1) + (1-3) + (3-1) + (3-1) = 4
(1-2),(3-2),(1-1),(2-1),(3-3),(3-2) these pairs
will give zero as their absolute difference is <= 1
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function sum() that takes an array (arr), sizeOfArray (n), and return an integer denoting the sum of f(a[i], a[j]) of all pairs. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ a[i] ≤ 10^{7}
"""

def calculate_pair_sum(arr, n):
    cnt = dict()
    ans = 0
    pre_sum = 0
    
    for i in range(n):
        ans += i * arr[i] - pre_sum
        pre_sum += arr[i]
        
        if arr[i] - 1 in cnt:
            ans -= cnt[arr[i] - 1]
        if arr[i] + 1 in cnt:
            ans += cnt[arr[i] + 1]
        
        if arr[i] not in cnt:
            cnt[arr[i]] = 0
        cnt[arr[i]] += 1
    
    return ans