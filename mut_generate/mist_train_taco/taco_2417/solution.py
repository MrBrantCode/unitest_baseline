"""
QUESTION:
Given an array A[]. The task is to find the maximum product possible with the subset of elements present in the array. The maximum product can be a single element also.
Since the product can be large, return it modulo (10^{9} + 7).
Example 1:
Input:
A[] = {-1, -1, -2, 4, 3}
Output: 24
Explanation: Maximum product will be ( -2 * -1 * 4 * 3 ) = 24
Example 2:
Input:
A[] = {-1, 0}
Output: 0
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findMaxProduct() which takes an array of size N and returns an integer.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 2 * 10^{4}
-10 <= A[i] <= 10
"""

def find_max_product(A):
    MOD = 10**9 + 7
    
    if len(A) == 1:
        return A[0] % MOD
    
    neg_arr = []
    pos_arr = []
    
    for num in A:
        if num < 0:
            neg_arr.append(num)
        elif num > 0:
            pos_arr.append(num)
    
    if len(neg_arr) % 2 != 0:
        neg_arr.remove(max(neg_arr))
    
    if not pos_arr and not neg_arr:
        return 0
    
    ans = 1
    for num in pos_arr:
        ans = (ans * num) % MOD
    for num in neg_arr:
        ans = (ans * num) % MOD
    
    return ans