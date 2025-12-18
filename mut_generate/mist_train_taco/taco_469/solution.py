"""
QUESTION:
Given an array arr[ ] of positive integers, the task is to find the maximum XOR value of the elements from all the possible subsets.
Example 1:
Input: N = 3, arr[] = {2, 4, 5}
Output: 7
Explanation: Subset {2, 5} has maximum xor
Example 2:
Input: N = 1, arr[] = {1}
Output: 1
Explanation: Subset {1} has maximum xor
Your Task:  
You don't need to read input or print anything. Complete the function maxXor() which takes N and array arr as input parameter and returns the maximum xor value.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N, arr[i] ≤ 10^{5}
"""

def max_xor(arr, N):
    start = 0
    for i in range(18, -1, -1):
        ma = -1
        k = -1
        for j in range(start, N):
            if arr[j] & 1 << i and (ma == -1 or ma < arr[j]):
                ma = arr[j]
                k = j
        if k == -1:
            continue
        (arr[k], arr[start]) = (arr[start], arr[k])
        start += 1
        for j in range(start, N):
            if arr[j] & 1 << i:
                arr[j] ^= ma
    ans = 0
    for j in range(N):
        if ans < ans ^ arr[j]:
            ans ^= arr[j]
    return ans