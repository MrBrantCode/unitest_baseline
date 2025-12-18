"""
QUESTION:
Given an array arr[] of size N of distinct elements and a number X, find if there is a pair in arr[] with product equal to X.
Example 1:
Input:
N = 4, X = 400
arr[] = {10, 20, 9, 40}
Output: Yes
Explanation: As 10 * 40 = 400.
Example 2:
Input:
N = 4, X = 30
arr[] = {-10, 20, 9, -40}
Output: No
Explanation: No pair with product 30.
Your Task:
You don't need to read input or print anything. Your task is to complete the function isProduct() which takes the arr[], n and x as input parameters and returns an boolean value denoting the answer.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ |arr_{i}| ≤ 10^{8}
0 ≤ X ≤ 10^{18}
"""

def has_product_pair(arr: list[int], x: int) -> bool:
    """
    Determines if there is a pair in the array `arr` whose product is equal to `x`.

    Parameters:
    - arr (list[int]): A list of distinct integers.
    - x (int): The product to be checked.

    Returns:
    - bool: True if there exists a pair with the product `x`, otherwise False.
    """
    for i in range(len(arr)):
        if arr[i] != 0 and x % arr[i] == 0 and (x // arr[i] in arr):
            return True
    return False