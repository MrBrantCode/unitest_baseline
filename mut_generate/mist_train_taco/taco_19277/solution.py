"""
QUESTION:
Given an array of integers of size n and an integer k, find all the pairs in the array whose absolute difference is divisible by k.
Example 1:
Input:
n = 3
arr[] = {3, 7, 11}
k = 4
Output:
3
Explanation:
(11-3) = 8 is divisible by 4
(11-7) = 4 is divisible by 4
(7-3) = 4 is divisible by 4
Example 2:
Input:
n = 4
arr[] = {1, 2, 3, 4}
k = 2
Output :
2
Explanation:
Valid pairs are (1,3), and (2,4).
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countPairs() which takes integers n, array arr[ ], integer k as input parameters and returns the number of pairs whose absolute difference is divisible by k.
Note: The answer may be large so use 64-bit integer. 
Expected Time Complexity: O(n + k)
Expected Auxiliary Space: O(k)
Constraints:
2 ≤ n ≤ 10^{5}
1 ≤ k,arr[i] ≤ 10^{5}
"""

def count_pairs_divisible_by_k(arr, k):
    modDic = {}
    result = 0
    
    # Count the occurrences of each remainder when divided by k
    for item in arr:
        resToCheck = item % k
        if resToCheck in modDic:
            modDic[resToCheck] += 1
        else:
            modDic[resToCheck] = 1
    
    # Calculate the number of valid pairs
    for count in modDic.values():
        if count > 1:
            result += count * (count - 1) // 2
    
    return result