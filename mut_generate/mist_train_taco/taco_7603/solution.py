"""
QUESTION:
Given two numbers M and N. The task is to find the position of the rightmost different bit in the binary representation of numbers.
Example 1: 
Input: M = 11, N = 9
Output: 2
Explanation: Binary representation of the given 
numbers are: 1011 and 1001, 
2nd bit from right is different.
Example 2:
Input: M = 52, N = 4
Output: 5
Explanation: Binary representation of the given 
numbers are: 110100 and 0100, 
5th-bit from right is different.
User Task:
The task is to complete the function posOfRightMostDiffBit() which takes two arguments m and n and returns the position of first different bits in m and n. If both m and n are the same then return -1 in this case.
Expected Time Complexity: O(max(log m, log n)).
Expected Auxiliary Space: O(1).
Constraints:
0 <= M <= 10^{9}
0 <= N <= 10^{9}
"""

def pos_of_rightmost_diff_bit(m: int, n: int) -> int:
    if m == n:
        return -1
    
    # XOR the two numbers to find the differing bits
    xor_result = m ^ n
    
    # Find the position of the rightmost set bit in the XOR result
    position = 1
    while xor_result & 1 == 0:
        xor_result >>= 1
        position += 1
    
    return position