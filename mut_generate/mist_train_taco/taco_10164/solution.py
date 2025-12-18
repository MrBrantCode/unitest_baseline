"""
QUESTION:
Given a number N and a bit number K, check if K^{th} index bit of N is set or not. A bit is called set if it is 1. Position of set bit '1' should be indexed starting with 0 from LSB side in binary representation of the number.
Note: Index is starting from 0.
Example 1:
Input: N = 4, K = 0
Output: No
Explanation: Binary representation of 4 is 100, 
in which 0^{th} index bit from LSB is not set. 
So, return false.
Example 2:
Input: N = 4, K = 2
Output: Yes
Explanation: Binary representation of 4 is 100, 
in which 2^{nd} index bit from LSB is set. 
So, return true.
Example 3:
Input: N = 500, K = 3
Output: No
Explanation: Binary representation of 500 is 
111110100, in which 3rd index bit from LSB is not set. 
So, return false.
Your task:
You don't have to read input or print anything. Your task is to complete the function checkKthbit that takes n and k as parameters and returns either true (if kth bit is set) or false(if kth bit is not set).
Expected Time Complexity: O(1).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 10^{9}
0 ≤ K ≤ floor(log_{2}(N) + 1)
"""

def is_kth_bit_set(n: int, k: int) -> bool:
    """
    Check if the k-th bit of the number n is set (i.e., 1).

    Parameters:
    - n (int): The number whose bits are to be checked.
    - k (int): The bit position (0-indexed) from the LSB to check.

    Returns:
    - bool: True if the k-th bit is set, False otherwise.
    """
    return (n >> k) & 1 == 1