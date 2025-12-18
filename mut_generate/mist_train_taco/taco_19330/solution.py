"""
QUESTION:
Given an interger array arr[] of size n and an interger k.In one operation, you can choose an index i where 0<i Return the maximum frequency of an element after using atmost k Increment operations.
 
Example 1:
Input:
n=3
arr[] = {2,2,4},k=4
Output: 3
Explanation: Apply two operations on index 0 and two operations
on index 1 to make arr[]={4,4,4}.Frequency of 4 is 3.
Example 2:
Input:
n=4
arr[] = {7,7,7,7},k=5
Output: 4
Explanation: It is optimal to not use any operation.
Frequency of 7 is 4.
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxFrequency() which takes the array arr[] ,interger n  and integer  k as input and returns the maximum frequency of an element.
Expected Time Complexity: O(nlogn).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ n,k ≤ 10^{5}
1 ≤ arr[i] ≤ 10^{6}
"""

def max_frequency(arr, k):
    arr.sort()
    left = 0
    total = 0
    res = 0
    
    for right in range(len(arr)):
        total += arr[right]
        
        while arr[right] * (right - left + 1) > total + k:
            total -= arr[left]
            left += 1
        
        res = max(res, right - left + 1)
    
    return res