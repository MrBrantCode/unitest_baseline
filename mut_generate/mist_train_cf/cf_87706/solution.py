"""
QUESTION:
Find the subarray with the largest sum in an integer array that has a length greater than or equal to k and the sum of the subarray is divisible by a given integer p.

Function name: find_subarray(arr, k, p)
Input: 
- arr: an integer array of length n
- k: the minimum length of the subarray
- p: the divisor of the sum of the subarray
Output: the subarray with the largest sum that meets the given requirements

Restrictions: 
- The array can contain negative numbers
- Time Complexity: O(n)
- Space Complexity: O(1)
"""

def find_subarray(arr, k, p):
    n = len(arr)
    max_sum = float('-inf')
    curr_sum = 0
    start = end = 0

    for i in range(n):
        curr_sum += arr[i]

        if curr_sum < 0:
            curr_sum = 0
            start = i + 1

        if curr_sum > max_sum:
            max_sum = curr_sum
            end = i

        if (end - start + 1) >= k and max_sum % p == 0:
            return arr[start:end+1]

    return None