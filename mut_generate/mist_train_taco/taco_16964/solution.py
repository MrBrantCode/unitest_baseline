"""
QUESTION:
Given two non-negative integers a and b. The problem is to check whether the two numbers differ at one-bit position only or not. If yes then the answer is 1, otherwise 0.
Example 1:
Input: a = 13, b = 9
Output: 1
Explanation: (13)_{10} = (1101)_{2}
(9)_{10} = (1001)_{2}
Both the numbers differ at one bit 
position only, i.e, differ at the 
3rd bit from the right.
Example 2:
Input: a = 15, b = 8
Output: 0
Explanation: (15)_{10} = (1111)_{2} 
(8)_{10} = (1000)_{2} 
Both the numbers differ at 3 bit
positions.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function DifferOne() which takes a, b as inputs and returns the answer.
Expected Time Complexity: O(max(log a, log b))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ a, b ≤ 10^{9}
"""

def differ_by_one_bit(a: int, b: int) -> int:
    # Convert both numbers to their binary representations
    binary_a = bin(a)[2:].zfill(30)
    binary_b = bin(b)[2:].zfill(30)
    
    # Count the number of differing bits
    differing_bits = sum(1 for bit_a, bit_b in zip(binary_a, binary_b) if bit_a != bit_b)
    
    # Check if the numbers differ by exactly one bit
    return 1 if differing_bits == 1 else 0