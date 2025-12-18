"""
QUESTION:
Given two arrays, arr1[] and arr2[] of sizes M and N respectively, find the length of the longest common increasing subsequence(LCIS). 
Example 1:
Input:
M = 4
Arr1[] = {3, 4, 9, 1}
N = 7
Arr2[] = {5, 3, 8, 9, 10, 2, 1}
Output: 2
Explanation: The longest increasing subsequence
that is common is {3, 9} and its length is 2.
Example 2:
Input:
M = 4
Arr1[] = {1, 1, 4, 3}
N = 4
Arr2[] = {1, 1, 3, 4}
Output: 2
Explanation: There are two common 
subsequences {1, 4} and {1, 3}
both of length 2.
Your Task:
You don't need to read input or print anything. Your task is to complete the function LCIS() which takes arr1[] and its size m, arr2[] and its size n as input parameters and returns length of LCIS.
 
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N)
Constraints:
1 <= M, N <= 10^{3}
1 <= Arr1[i], Arr2[i] <= 10^{3}
"""

def find_lcis_length(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    
    # Initialize a table to store the length of LCIS ending at each element of arr2
    table = [0] * m
    
    for i in range(n):
        current = 0
        for j in range(m):
            if arr1[i] == arr2[j]:
                if current + 1 > table[j]:
                    table[j] = current + 1
            if arr1[i] > arr2[j]:
                if table[j] > current:
                    current = table[j]
    
    # The result is the maximum value in the table
    result = max(table)
    
    return result