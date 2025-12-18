"""
QUESTION:
Given an array and a number k, find the largest sum of the subarray containing at least k numbers. It may be assumed that the size of array is at-least k.
 
Example 1:
Input : 
n = 4
arr[] = {-4, -2, 1, -3}
k = 2
Output : 
-1
Explanation :
The sub array is {-2, 1}
 
Example 2:
Input :
n = 6 
arr[] = {1, 1, 1, 1, 1, 1}
k = 2
Output : 
6
Explanation :
The sub array is {1, 1, 1, 1, 1, 1}
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function maxSumWithK() which takes the array A[], its size N and an integer K as inputs and returns the value of the largest sum of the subarray containing at least k numbers.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1<=n<=10^{5}
-10^{5}<=a[i]<=10^{5}
1<=k<=n
"""

def max_sum_with_k(arr, k):
    def kandane(a):
        n = len(a)
        res = [0] * n
        aux_sum = 0
        max_sum = float('-inf')
        for i in range(n):
            aux_sum += a[i]
            if aux_sum < a[i]:
                aux_sum = a[i]
            res[i] = aux_sum
        return res

    n = len(arr)
    res = kandane(arr)
    beg, end = 0, 0
    aux_sum = 0
    max_sum = float('-inf')
    
    while end < n:
        aux_sum += arr[end]
        if end - beg + 1 == k:
            temp = res[beg - 1] if beg - 1 >= 0 else float('-inf')
            ans = max(aux_sum, aux_sum + temp)
            max_sum = max(max_sum, ans)
            aux_sum -= arr[beg]
            beg += 1
        end += 1
    
    return max_sum