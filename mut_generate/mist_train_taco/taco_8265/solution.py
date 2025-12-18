"""
QUESTION:
Given an array arr[] of size N. Find the maximum value of arr[j] – arr[i] + arr[l] – arr[k], such that i < j < k < l.
Example 1:
Input
N = 3
Arr[]  = {1, 2, 3}
Output:-1
Explanation: 
N<4 so no such i,j,k,l is possible.
 
Example 2:
Input:
N = 5
Arr[] = {4, 8, 9, 2, 20}
Output: 23
Explanation:
Here i = 0, j = 2, k = 3, l = 4 so
arr[j] – arr[i] + arr[l] – arr[k] 
= 9 – 4 + 20 – 2 = 23
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findMaxValue() which takes the array arr[] and its size N as input parameters and returns the maximum value of arr[j] – arr[i] + arr[l] – arr[k].
 
Expected Time Complexity : O(N)
Expected Auxiliary Space : O(N)
 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A[i] ≤ 10^{5}
"""

def find_max_value(arr, n):
    MIN = -100000000
    
    if n < 4:
        return -1
    
    table1 = [MIN] * (n + 1)
    table2 = [MIN] * n
    table3 = [MIN] * (n - 1)
    table4 = [MIN] * (n - 2)
    
    for i in range(n - 1, -1, -1):
        table1[i] = max(table1[i + 1], arr[i])
    
    for i in range(n - 2, -1, -1):
        table2[i] = max(table2[i + 1], table1[i + 1] - arr[i])
    
    for i in range(n - 3, -1, -1):
        table3[i] = max(table3[i + 1], table2[i + 1] + arr[i])
    
    for i in range(n - 4, -1, -1):
        table4[i] = max(table4[i + 1], table3[i + 1] - arr[i])
    
    return table4[0]