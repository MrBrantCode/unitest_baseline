"""
QUESTION:
Given an array Arr of length N, return the count of number of contiguous subarrays for which the sum and product of elements are equal.
Example 1:
Input:
N = 5
Arr[] = {1, 2, 3, 4, 5}
Output: 6
Explanation: All 6 subarrays having sum of
elements  equals to the product of
elements are: {1}, {2}, {3}, {4}, {5},
{1, 2, 3}
Your Task:
Complete the function numOfsubarrays() which takes an array arr, an integer n, as input parameters and returns an integer denoting the answer. You don't to print answer or take inputs.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10
1 <= Arr[i] <= 10 where 1 <= i <= N
"""

def count_equal_sum_product_subarrays(arr, n):
    output = 0
    for i in range(n):
        summa = 0
        product = 1
        for j in range(i, n):
            summa += arr[j]
            product *= arr[j]
            output += summa == product
    return output