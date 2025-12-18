"""
QUESTION:
Given an array arr[] of length N, find the lowest number which has both the maximum and minimum of the array as it's divisor.
 
Example 1:
Input:
N = 4
arr[] = {3, 4, 8, 6}
Output:
24
Explanation:
Minimum of the array is 3, while the
maximum is 8. The lowest number which has
both 3 and 8 as divisors is 24.
Example 2:
Input:
N = 2
arr[] = {1, 8}
Output:
8
Explanation:
Minimum of the array is 1, while the
maximum is 8. The lowest number which has
both 1 and 8 as divisors is 8.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function getNum() which takes an Integer N and an array arr[] of size N as input and returns the integer.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
1 <= arr[i] <= 10^{4}
"""

def find_lowest_common_multiple(arr, N):
    # Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)
    
    # Start with the maximum value as the initial candidate
    candidate = max_val
    
    # Loop until we find a number that is divisible by both min_val and max_val
    while True:
        if candidate % min_val == 0 and candidate % max_val == 0:
            return candidate
        candidate += 1