"""
QUESTION:
Given a sequence of non-negative integers, find the subsequence of length 3 having maximum product, with the elements of the subsequence being in increasing order.
 
Example 1:
Ã¢â¬â¹Input:
n = 8
arr[ ] = {6, 7, 8, 1, 2, 3, 9, 10}
Output:
8 9 10
Explanation: 3 increasing elements of 
the given arrays are 8,9 and 10 which 
forms the subsequence of size 3 with 
maximum product.
Ã¢â¬â¹Example 2:
Input:
n = 4
arr[ ] = {3, 4, 2, 1} 
Output:
Not Present 
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function maxProductSubsequence() that takes an array arr, sizeOfArray n, and return the subsequence of size 3 having the maximum product, numbers of subsequence being in increasing order. If no such sequence exists, return "-1". The driver code takes care of the printing.
Expected Time Complexity: O(N*LOG(N)).
Expected Auxiliary Space: O(N).
Constraints:
1 <= N <= 10^{5}
1 <= Arr[i] <= 10^{5}
"""

from bisect import bisect_left

def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i:
        return i - 1
    else:
        return -1

def findMaximumBefore(arr, n):
    res = [-1] * (n + 1)
    lst = []
    lst.append(arr[0])
    for i in range(1, n):
        idx = BinarySearch(lst, arr[i])
        if idx != -1:
            res[i] = lst[idx]
        lst.insert(idx + 1, arr[i])
    return res

def max_product_subsequence(arr, n):
    if n < 3:
        return ["-1"]
    
    small = findMaximumBefore(arr, n)
    large = [0] * n
    large[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        large[i] = max(large[i + 1], arr[i])
    
    res = -1
    ans = ["-1"]
    for i in range(1, n - 1):
        if small[i] != -1 and large[i + 1] > arr[i]:
            if res < small[i] * arr[i] * large[i + 1]:
                res = small[i] * arr[i] * large[i + 1]
                ans = [small[i], arr[i], large[i + 1]]
    
    return ans