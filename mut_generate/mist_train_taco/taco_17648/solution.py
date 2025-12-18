"""
QUESTION:
The hiring team aims to find 3 candidates who are great collectively. Each candidate has his or her ability expressed as an integer. 3 candidates are great collectively if product of their abilities is maximum. Given abilities of N candidates in an array arr[], find the maximum collective ability from the given pool of candidates.
Example 1:
Input:
N = 5
Arr[] = {10, 3, 5, 6, 20}
Output: 1200
Explanation:
Multiplication of 10, 6 and 20 is 1200.
Example 2:
Input:
N = 5
Arr[] = {-10, -3, -5, -6, -20}
Output: -90
Explanation:
Multiplication of -3, -5 and -6 is -90.
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxProduct() which takes the array of integers arr[] and n as input parameters and returns the maximum product.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
3 ≤ N ≤ 10^{7}
-10^{5} ≤ Arr[i] ≤ 10^{5}
"""

def max_collective_ability(arr, n):
    # Sort the array to easily access the largest and smallest elements
    arr.sort()
    
    # Calculate the maximum product of three largest elements
    max_product_largest = arr[-1] * arr[-2] * arr[-3]
    
    # Calculate the product of two smallest elements and the largest element
    max_product_small_large = arr[0] * arr[1] * arr[-1]
    
    # Return the maximum of the two calculated products
    return max(max_product_largest, max_product_small_large)