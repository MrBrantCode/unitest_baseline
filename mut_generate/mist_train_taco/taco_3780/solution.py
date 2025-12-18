"""
QUESTION:
Given an array of even size consisting of positive integers. Your task is to find the sum after sorting the array, such that the sum of product of alternate elements is minimum.
 
Example 1:
Input:
8
9 2 8 4 5 7 6 0
Output:
74
Explanation:
Required sum can be obtained as
9*0 + 8*2 + 7*4 + 6*5 which
is equal to 74.
 
Example 2:
Input:
4
1 2 3 4
Output:
10
Explanation:
1*4 + 2*3 = 10
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function altPoduct() which takes the array A[] and its size N as inputs and returns the minimum sum.
Expected Time Complexity: O(N. log(N))
Expected Auxiliary Space: O(1)
 
Constraints:
2 ≤ N ≤ 10^{5}
1 ≤ A_{i} ≤ 10^{7}
N is always even
"""

def minimum_alternate_product_sum(arr, n):
    arr.sort()
    summ = 0
    for i in range(n // 2):
        summ += arr[i] * arr[-(i + 1)]
    return summ