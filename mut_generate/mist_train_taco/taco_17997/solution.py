"""
QUESTION:
Given an array of N positive integers, find GCD of all the array elements.
Example 1:
Input: N = 3, arr[] = {2, 4, 6}
Output: 2
Explanation: GCD of 2,4,6 is 2.
Example 2:
Input: N = 1, arr[] = {1}
Output: 1
Explanation: Greatest common divisor of
all the numbers is 1.
Your Task:  
You don't need to read input or print anything. Complete the function gcd()which takes N and array as input parameters and returns the gcd.
Expected Time Complexity: O(N logN)
Expected Auxiliary Space: O(1) 
Constraints:
1 ≤ N, arr[i] ≤ 10^{5}
"""

def find_gcd(a: int, b: int) -> int:
    """Helper function to find the GCD of two numbers."""
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def find_array_gcd(arr: list[int]) -> int:
    """
    Function to find the GCD of all elements in the array.

    Parameters:
    - arr: A list of positive integers.

    Returns:
    - An integer representing the GCD of all elements in the array.
    """
    if not arr:
        return 0  # Edge case: empty array
    
    result = arr[0]
    for num in arr[1:]:
        result = find_gcd(result, num)
        if result == 1:
            return 1  # Early exit if GCD becomes 1
    
    return result