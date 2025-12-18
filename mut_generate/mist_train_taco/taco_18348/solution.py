"""
QUESTION:
Given an array Arr of size N containing positive integers. Find the maximum sum of a subsequence such that no two numbers in the sequence should be adjacent in the array. 
Example 1:
Input:
N = 6
Arr[] = {5, 5, 10, 100, 10, 5}
Output: 110
Explanation: If you take indices 0, 3
and 5, then Arr[0]+Arr[3]+Arr[5] =
5+100+5 = 110.
 
Example 2:
Input:
N = 4
Arr[] = {3, 2, 7, 10}
Output: 13
Explanation: 3 and 10 forms a non
continuous  subsequence with maximum
sum.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function findMaxSum() which takes the array of integers arr and n as parameters and returns an integer denoting the answer. It is guaranteed that your answer will always fit in the 32-bit integer.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ N ≤ 10^{6}
1 ≤ Arr_{i} ≤ 10^{7}
"""

def find_max_sum(arr, n):
    if n < 3:
        m = arr[0]
        for i in range(n):
            m = max(m, arr[i])
        return m
    
    d = [arr[0], arr[1], arr[2] + arr[0]]
    for i in range(3, n):
        d[i % 3] = max(d[(i - 2) % 3] + arr[i], d[(i - 3) % 3] + arr[i])
    
    return max(d[(n - 1) % 3], d[(n - 2) % 3], d[(n - 3) % 3])