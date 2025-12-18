"""
QUESTION:
Given an array arr[] of size N, find the first digit from the left of the product of these N integers.
Example 1:
Input: N = 4, arr[] = {5, 8, 3, 7}
Output: 8
Explanation: Produt is 840
Example 2:
Input: N = 3, arr[] = {6, 7, 9} 
Output: 3
Explanation: Produt is 378
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function firstDigit() which takes N and array arr[] as input parameters and returns the left digit of product.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N, arr[i] ≤ 10^{5}
Test cases have been designed such that there is no precision ambiguity.
"""

def first_digit_of_product(arr, n):
    p = 1
    for i in range(n):
        p *= arr[i]
        d = str(p)
        p = int(d[:6])  # Truncate to avoid overflow
    return int(str(p)[0])