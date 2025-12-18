"""
QUESTION:
Given an array arr[] of n integers containing only 0 and 1. Write a program to find the minimum toggles (switch from 0 to 1 or vice-versa) required such the array the array become partitioned, i.e., it has first 0s then 1s. There should be at least one 0 in the beginning, and there can be zero or more 1s in the end.
Example 1:
Input: n = 5
arr = {1, 0, 1, 1, 0}
Output: 2
Explaination: The changed array will be 
{0, 0, 1, 1, 1}. So the number of toggles 
here required is 2.
Example 2:
Input: n = 7
arr = {0, 1, 0, 0, 1, 1, 1}
Output: 1
Explaination: The changed array will be 
{0, 0, 0, 0, 1, 1, 1}. Required toggles are 1.
Your Task:
You do not need to read input or print output. Your task is to complete the function minToggle() which takes n and arr as input parameters and returns the minimum number of toggles required to modify the array. 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)
Constraints:
1 ≤ n ≤ 10^{5}
1 ≤ arr[i] ≤ 100
"""

def min_toggles_to_partition(arr):
    n = len(arr)
    pref = [0] * n
    suff = [0] * n
    
    # Calculate prefix sums of 1s
    pref[0] = arr[0]
    for i in range(1, n):
        pref[i] = pref[i - 1] + arr[i]
    
    # Calculate suffix sums of 1s
    suff[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suff[i] = suff[i + 1] + arr[i]
    
    # Calculate the minimum toggles required
    ans = float('inf')
    for i in range(n - 1):
        ans = min(ans, pref[i] + (n - i - 1) - suff[i + 1])
    ans = min(ans, pref[n - 1])
    
    return ans