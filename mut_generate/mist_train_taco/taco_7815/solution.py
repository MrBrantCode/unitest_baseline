"""
QUESTION:
You are given an array arr[] of numbers of size N. You need to multiply these numbers and find the remainder when the product of these numbers is divided by a number K.
 
Example 1:
Input:
N = 3
arr[] = {4, 6, 7}
K = 3
Output:
0
Explanation:
4*6*7 = 168%3 = 0
Example 2:
Input:
N = 2
arr[] = {1, 6}
K = 5
Output:
1
Explanation:
1*6 = 6%5 = 1
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function remArray() which takes a integers N, an array arr[] of size N and another integer K as input and returns the Product of the array modulo K.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N,K,arr[i] <= 10^{5}
"""

def calculate_product_modulo(arr, K):
    pro = 1
    for num in arr:
        pro = pro * num % K
    return pro % K